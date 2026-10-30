#!/usr/bin/env python3
"""Derive category subsets from the main dataset, e.g. code-switching only or tech only.

The main dataset, danielrosehill/Read-Aloud-Voice-Sentences, holds every take (Parquet on `main` since
2026-10-30; this reads either that or an older audiofolder revision and writes audiofolders). Each row has
a `categories` list (code_switch, tech, names, email, message, general, homophone, long), and
a row can have several. This script copies the rows whose categories include the one you
ask for into a separate dataset folder with the same layout, ids, columns and train/test
split:

    <out>/<category>/data/<split>/audio/<id>.wav
    <out>/<category>/data/<split>/metadata.jsonl

That is how the published subsets are built:
  code_switch -> danielrosehill/English-Hebrew-Codeswitching-Sentences
  tech        -> danielrosehill/Tech-Sentences
Those two hold phone takes only, so imported rows (`mode == "import"`, recorded in 2025 on a
desktop microphone) are left out by default; pass --include-imports to keep them.

Usage:
  uv run --with huggingface_hub python scripts/split_subsets.py                 # code_switch + tech -> ./subsets
  uv run --with huggingface_hub python scripts/split_subsets.py -c general --metadata-only
  uv run --with huggingface_hub python scripts/split_subsets.py -c code_switch --push <you>/<new-dataset>

--metadata-only writes the metadata.jsonl files without downloading audio, which is enough to
count rows and minutes. --push uploads the folder to a Hugging Face dataset you own (needs
`hf auth login`); the published subsets are maintained by the project, not by this script.
"""
import argparse, json
from pathlib import Path

from huggingface_hub import HfApi, hf_hub_download

MAIN = "danielrosehill/Read-Aloud-Voice-Sentences"
SPLITS = ("train", "test")


INDEX_KEYS = ("shard", "audio_path", "audio_offset", "audio_length")


def rows(split, revision):
    """Metadata rows of a split. The dataset is Parquet since 2026-10-30: its index meta/<split>.jsonl has
    the old metadata.jsonl rows with `audio_path` in place of `file_name`, plus `shard` and the audio file's
    byte range in it. An older revision is an audiofolder (data/<split>/metadata.jsonl)."""
    from huggingface_hub.errors import EntryNotFoundError
    try:
        p = hf_hub_download(MAIN, f"meta/{split}.jsonl", repo_type="dataset", revision=revision)
    except EntryNotFoundError:
        p = hf_hub_download(MAIN, f"data/{split}/metadata.jsonl", repo_type="dataset", revision=revision)
    out = [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]
    for r in out:
        if "audio_path" in r:
            r["file_name"] = r["audio_path"]
    return out


def fetch_audio(split, sel, d, revision):
    """Write each selected take's audio to d/<file_name>, skipping files already there. Parquet: download
    only the shards that hold a missing take and cut each file out by its byte range (it is stored verbatim).
    Audiofolder: one download per file."""
    missing = [r for r in sel if not (d / r["file_name"]).exists()]
    shards = {}
    for r in missing:
        if "shard" in r:
            shards.setdefault(r["shard"], []).append(r)
        else:
            src = hf_hub_download(MAIN, f"data/{split}/{r['file_name']}", repo_type="dataset", revision=revision)
            (d / r["file_name"]).write_bytes(Path(src).read_bytes())
    for shard, rs in shards.items():
        with open(hf_hub_download(MAIN, shard, repo_type="dataset", revision=revision), "rb") as f:
            for r in rs:
                f.seek(r["audio_offset"])
                (d / r["file_name"]).write_bytes(f.read(r["audio_length"]))


def wanted(r, cat, include_imports):
    return cat in r.get("categories", []) and (include_imports or r.get("mode") != "import")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("-c", "--category", action="append", help="category to extract; repeatable (default: code_switch, tech)")
    ap.add_argument("-o", "--out", default="subsets")
    ap.add_argument("--revision", default="main", help="dataset revision (branch or commit sha)")
    ap.add_argument("--include-imports", action="store_true")
    ap.add_argument("--metadata-only", action="store_true")
    ap.add_argument("--push", metavar="REPO", help="upload the (single) subset to this HF dataset repo")
    a = ap.parse_args()
    cats = a.category or ["code_switch", "tech"]
    if a.push and len(cats) != 1:
        ap.error("--push takes exactly one --category")

    a.revision = HfApi().dataset_info(MAIN, revision=a.revision).sha  # one commit: index and shards agree
    data = {s: rows(s, a.revision) for s in SPLITS}
    summary = {}
    for cat in cats:
        root = Path(a.out) / cat
        summary[cat] = {}
        for split, rs in data.items():
            sel = [r for r in rs if wanted(r, cat, a.include_imports)]
            d = root / "data" / split
            (d / "audio").mkdir(parents=True, exist_ok=True)
            with open(d / "metadata.jsonl", "w", encoding="utf-8") as f:
                f.writelines(json.dumps({"file_name": r["file_name"], **{k: v for k, v in r.items() if k not in INDEX_KEYS}},
                                        ensure_ascii=False) + "\n"
                             for r in sel)
            if not a.metadata_only:
                fetch_audio(split, sel, d, a.revision)
            summary[cat][split] = {"rows": len(sel), "minutes": round(sum(r["duration_s"] for r in sel) / 60, 1)}
        if a.push:
            api = HfApi()
            api.create_repo(a.push, repo_type="dataset", exist_ok=True)
            api.upload_folder(repo_id=a.push, repo_type="dataset", folder_path=str(root),
                              commit_message=f"Subset '{cat}' of {MAIN}@{a.revision}")
            summary[cat]["pushed_to"] = a.push
    print(json.dumps({"source": MAIN, "revision": a.revision, "out": a.out, "subsets": summary}, indent=1))


if __name__ == "__main__":
    main()
