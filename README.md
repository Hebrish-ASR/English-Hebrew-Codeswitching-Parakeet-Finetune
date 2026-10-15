# English-Hebrew-Codeswitching-Parakeet-Finetune

Public tracker for an **English-Hebrew code-switching** fine-tune of
[`nvidia/parakeet-tdt-0.6b-v2`](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v2): speech
recognition that gets the Hebrew words right when an English speaker in Israel drops them
into English: *"pick up some bamba from the makolet"*, *"I have to go to Bituach Leumi
tomorrow"*. This repo records where the project stands and links to the datasets, the
related tools and, once it is released, the model. The working code lives in a separate
private repository.

> **A real result:** the speaker recorded this in the [demo Space](https://huggingface.co/spaces/danielrosehill/English-Hebrew-Codeswitching-Parakeet-Demo) (2026-10-15):
>
> | | Transcript |
> |---|---|
> | Stock Parakeet v2 | I want to go to the **Micollette** today to buy my groceries. |
> | **This fine-tune** | I want to go to the **makolet** today to buy my groceries. |
>
> *Makolet* (מכולת) is the Israeli corner grocery shop. Stock v2 has never heard the word,
> so it guesses an English-looking name; the fine-tune writes the word itself.

[![Download v2 GGUF Q8_0 (730 MB)](https://img.shields.io/badge/⬇_Download_v2-GGUF_Q8__0_·_730_MB_·_recommended-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/danielrosehill/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching/resolve/main/gguf/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching-Q8_0.gguf)
[![Download v2 GGUF Q4_K_M (475 MB)](https://img.shields.io/badge/⬇_Download_v2-GGUF_Q4__K__M_·_475_MB-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/danielrosehill/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching/resolve/main/gguf/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching-Q4_K_M.gguf)
[![Get Offline Voice Input on Google Play](https://img.shields.io/badge/Android_app-Offline_Voice_Input-34A853?style=for-the-badge&logo=googleplay&logoColor=white)](https://play.google.com/store/apps/details?id=dev.notune.transcribe)
[![Try the demo](https://img.shields.io/badge/Try_it-Demo_Space-FF9D00?style=for-the-badge&logo=huggingface&logoColor=white)](https://huggingface.co/spaces/danielrosehill/English-Hebrew-Codeswitching-Parakeet-Demo)
[![Model card](https://img.shields.io/badge/Model-.nemo_·_2.47_GB-555555?style=for-the-badge&logo=nvidia&logoColor=76B900)](https://huggingface.co/danielrosehill/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching)

### Which file should I download?

All links below are the **latest version, v2** (2026-10-15); they always point to the newest
release. Earlier versions, with permanent links, are under **Version history**.

| You want to… | Download | Run it with |
|---|---|---|
| **Dictate on an Android phone** | **[Q8_0 GGUF](https://huggingface.co/danielrosehill/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching/resolve/main/gguf/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching-Q8_0.gguf)** (730 MB) | [Offline Voice Input](https://play.google.com/store/apps/details?id=dev.notune.transcribe) |
| Dictate on an Android phone with little memory (≤ 4 GB RAM), or if Q8_0 is too slow | [Q4_K_M GGUF](https://huggingface.co/danielrosehill/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching/resolve/main/gguf/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching-Q4_K_M.gguf) (475 MB) | Offline Voice Input |
| **Dictate on a Linux desktop** | **[Q8_0 GGUF](https://huggingface.co/danielrosehill/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching/resolve/main/gguf/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching-Q8_0.gguf)** (730 MB) | [Handy](https://github.com/cjpais/Handy) |
| Transcribe in Python, on a GPU, or fine-tune further | [`.nemo`](https://huggingface.co/danielrosehill/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching/resolve/main/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching.nemo) (2.47 GB, full precision) | [NVIDIA NeMo](https://github.com/NVIDIA-NeMo/Speech) |

**If unsure, take Q8_0.** It is the closest to full accuracy that still runs on a phone, and
on desktop CPUs it was also *faster* than Q4_K_M: about 3× realtime against 1.4× on 8 cores.
On five held-out test clips, Q8_0 matched the `.nemo` word for word; Q4_K_M differed on one word (v2, 2026-10-15). Speed on phones has not
been measured yet. ONNX exports for sherpa-onnx apps (Voxtype, Dictus) are not published
yet.

## Use it on Android (5 minutes)

1. Install **Offline Voice Input** ([Google Play](https://play.google.com/store/apps/details?id=dev.notune.transcribe),
   [source](https://github.com/notune/android_transcribe_app), MIT). It is the one Android
   voice keyboard found (2026-10-15) that loads arbitrary Parakeet weights, and it runs
   fully offline.
2. On the phone, download the **[Q8_0 GGUF](https://huggingface.co/danielrosehill/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching/resolve/main/gguf/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching-Q8_0.gguf)** (730 MB, recommended). The
   **[Q4_K_M GGUF](https://huggingface.co/danielrosehill/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching/resolve/main/gguf/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching-Q4_K_M.gguf)** (475 MB) is for phones short on memory.
3. In the app, import a model, pick the downloaded `.gguf` and select it.
4. Use it in either of two ways:
   - set the app as the system **voice input**; or
   - use a keyboard whose mic key opens it: SwiftKey, HeliBoard or FlorisBoard. Gboard's
     mic button cannot hand speech to it.
5. Set the app's battery optimisation to **Unrestricted**, so Android does not kill it
   between dictations.

Both GGUFs were converted with transcribe.cpp **v0.1.3**, the version the app links. On five
held-out test clips, Q8_0 gave word-for-word the same transcripts as the PyTorch model and
Q4_K_M differed on one word (v2, checked 2026-10-15).

**Linux:** [Handy](https://github.com/cjpais/Handy) loads the same GGUF. Copy it into
`~/.local/share/com.pais.handy/models/` with its own file name; a name that matches a stock
catalogue file is treated as the stock model.

**Status (2026-10-15): v2 published** (120 min of code-switching). Data collection continues toward v3 at 180 min.
Model: [`danielrosehill/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching`](https://huggingface.co/danielrosehill/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching)

## The problem

Stock Parakeet v2 is strong on English, but it has never seen romanized Hebrew. A Hebrew
word in English speech comes out as whatever English words sound closest. The v2 tokenizer
has no Hebrew characters, so the fix is to teach the model one **romanized spelling** per
Hebrew word, from read-aloud sentences recorded by the speaker on the phone that will run
the model.

## Scope

- **In scope:** Hebrew words inside English speech, for one speaker (an English speaker
  living in Jerusalem), on an Android phone.
- **Out of scope:** tech vocabulary, homophones, disfluency removal and paragraph
  formatting. Some recording sessions capture tech sentences too, for convenience; they
  are published in the main dataset.

## Training mix

Fine-tuning a pretrained model on code-switched speech alone badly damages its English. In
one study, Whisper-small went from 3.4% to 13.3% WER on LibriSpeech after fine-tuning on
code-switched data only. The literature consistently finds that mixing monolingual data in
works better. Mixing in as little as 10% original-domain data has been shown to cut
forgetting sharply, while too much monolingual data hurts code-switching. The target
balance, by audio duration:

| Share | Data |
|---|---|
| ~70% | Code-switching takes |
| ~20% | The speaker's own monolingual English, recorded on the same phone |
| ~10% | Public English replay (LibriSpeech or Common Voice) |

No paper gives a ratio for this exact case (one speaker, English as the main language, one
or two Hebrew words per sentence), so the pilot compares 0%, 15% and 30% English and keeps
the best on both test sets: held-out code-switching and general English.

Sources: [Liu et al. 2025](https://arxiv.org/abs/2509.24310),
[Shah et al. 2020](https://arxiv.org/abs/2006.00782),
[Pekarek Rosin & Siegert 2023](https://arxiv.org/abs/2307.07280),
[CS ASR systematic review 2025](https://arxiv.org/abs/2507.07741).

## Training data (v2)

Everything v2 was trained on, by dataset. The training job pins one revision of
`Read-Aloud-Voice-Sentences` (`3bdaa2a50d52`) and adds public English replay at train time.

| Dataset | Whose | What v2 used from it | Licence |
|---|---|---|---|
| [`Read-Aloud-Voice-Sentences`](https://huggingface.co/datasets/danielrosehill/Read-Aloud-Voice-Sentences) | Mine | **The training source.** 1,248 code-switching clips (120.1 min): 754 phone takes (87.6 min), 55 laptop takes (5.7 min) and 439 recordings imported from the desktop-mic round below (26.8 min). Plus 224 clips of my own monolingual English (28.7 min). | CC-BY-4.0 |
| [`English-Hebrew-Codeswitching-Sentences`](https://huggingface.co/datasets/danielrosehill/English-Hebrew-Codeswitching-Sentences) | Mine | The code-switching phone takes, published on their own. Same audio as above, not extra data. | CC-BY-4.0 |
| [`English-Hebrew-Mixed-Sentences`](https://huggingface.co/datasets/danielrosehill/English-Hebrew-Mixed-Sentences) | Mine | An earlier desktop-mic round (2025-11-17). 439 of its recordings are imported into `Read-Aloud-Voice-Sentences` with fixed transcripts, and counted there. | MIT |
| [LibriSpeech](https://huggingface.co/datasets/openslr/librispeech_asr) `train-clean-100` with [LibriSpeech-PC](https://www.openslr.org/145/) transcripts | Public | 17.3 min of English replay, so the model keeps general English. LibriSpeech-PC supplies the cased, punctuated transcripts. `test-clean` (200 utterances) is used only for evaluation. | CC-BY-4.0 |

Evaluation uses the held-out test split of `Read-Aloud-Voice-Sentences` (121 code-switching
clips, term-disjoint) and is never trained on.

## Links

| What | Link | Status |
|---|---|---|
| Base model | [`nvidia/parakeet-tdt-0.6b-v2`](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v2) | Upstream |
| **Fine-tuned model** | [`danielrosehill/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching`](https://huggingface.co/danielrosehill/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching) | v2, 2026-10-15: `.nemo` plus GGUF Q8_0 and Q4_K_M. CC-BY-4.0, like the base model. v1 is in the repo history. |
| Android app that loads it | [Offline Voice Input](https://play.google.com/store/apps/details?id=dev.notune.transcribe) ([source](https://github.com/notune/android_transcribe_app)) | Imports the GGUF; works as a voice keyboard and as the system voice input |
| **Training data**: code-switching takes | [`danielrosehill/English-Hebrew-Codeswitching-Sentences`](https://huggingface.co/datasets/danielrosehill/English-Hebrew-Codeswitching-Sentences) | Live, synced on every push |
| **Demo**: stock v2 vs the fine-tune, side by side | [Space: `English-Hebrew-Codeswitching-Parakeet-Demo`](https://huggingface.co/spaces/danielrosehill/English-Hebrew-Codeswitching-Parakeet-Demo) | Live (ZeroGPU) |
| Browser for the training data | [Space: `English-Hebrew-Codeswitching-Browser`](https://huggingface.co/spaces/danielrosehill/English-Hebrew-Codeswitching-Browser) | Live |
| Earlier round: code-switched recordings (desktop mic) | [`danielrosehill/English-Hebrew-Mixed-Sentences`](https://huggingface.co/datasets/danielrosehill/English-Hebrew-Mixed-Sentences) | Its sentences were re-read on the phone; its recordings may join training |
| **Hebrew-Latin token classifier**: detects Hebrew words written in Latin letters inside English | [GitHub: `Hebrew-Latin-Token-Classifier`](https://github.com/danielrosehill/Hebrew-Latin-Token-Classifier) | Its lexicon sets the canonical romanized spelling of every Hebrew word in the transcripts |
| Span review tool for the classifier | [Space: `hebrew-latin-span-review`](https://huggingface.co/spaces/danielrosehill/hebrew-latin-span-review) | Live |
| All takes from the capture sessions: code-switching, the speaker's monolingual English, and out-of-scope categories | [`danielrosehill/Read-Aloud-Voice-Sentences`](https://huggingface.co/datasets/danielrosehill/Read-Aloud-Voice-Sentences) | Live; source of the ~20% own-English share. The code-switching dataset above is its subset. |

## Lifecycle

| Stage | State | Notes |
|---|---|---|
| 1. Plan | Done, 2026-10-14 | Read-aloud sentences recorded on the target phone, NeMo fine-tune, on-device export |
| 2. Capture app | Done, 2026-10-14 | A phone web app in the style of Common Voice: read a sentence, record it, review, next. Takes are pushed to Hugging Face in batches. |
| 3. Data collection | **In progress** | See "Data so far" |
| 4. Baseline | Done, 2026-10-15 | Stock v2 got 28% of Hebrew term occurrences right across 615 terms |
| 5. Pilot fine-tune | Done, 2026-10-15 | v1, 77 min of code-switching |
| 6. Retrains | v2 done, 2026-10-15 | v2 at 120 min, ~28% English. Next: v3 at 180 min, with the 0/15/30% English comparison. |
| 7. On-device export | GGUF done, 2026-10-15 | v2 re-exported: Q8_0 identical to PyTorch on 5 test clips, Q4_K_M off by one word. Phone test pending. |
| 8. Release | v2 released | The base model is CC-BY-4.0, so fine-tunes are published openly |

## Results

**v2** (run `r2-en30`, 2026-10-15) was trained from stock v2 on 120 min of code-switching,
29 min of the speaker's English and 17 min of LibriSpeech replay. It took 23 minutes on one
GPU. Both models were scored on the current test split (121 code-switching clips).

| Test set | Stock v2 | Fine-tune v2 |
|---|---|---|
| Code-switching, held-out test (WER) | 9.9% | **4.8%** |
| Hebrew terms **never seen in training**: share correct | 29% | **50%** |
| Hebrew terms seen in training: share correct | 38% | **75%** |
| Speaker's plain English (WER) | 2.7% | 2.4% |
| LibriSpeech test-clean (WER) | 1.2% | 1.1% |
| Long form, ~3-minute files (WER) | 7.8% | **4.5%** |

![Word error rate, stock v2 vs the fine-tune](figures/wer.png)

![Hebrew terms transcribed correctly, stock v2 vs the fine-tune](figures/terms.png)

v1 and v2 side by side, on the same test split, are under **Version history** below.

WER here is lowercase with punctuation removed. English did not get worse. The jump on
unseen terms suggests the model learned how this speaker's Hebrew maps to the
romanization, not only the training words.

![How stock v2 handles 615 Hebrew terms](figures/baseline_terms.png)

The baseline also showed which words matter. Stock v2 already gets 165 of 615 terms right
every time: mostly names, well-known places and words that are already English (Shabbat,
Pesach, Bamba). It never gets 390 right: Misrad Hapnim, Bituach Leumi, tzaharon, rofe
mishpacha, Motzei Shabbat, Pikud Haoref. Recording now concentrates on the second group.

### Version history

Every version is re-scored on the **same** test split as the newest one, so the rows below
compare like with like. The download links at the top of this page are always the latest version;
the links in the last row stay pinned to each version's files forever.

![Word error rate by version](figures/versions_wer.png)

![Hebrew terms transcribed correctly, by version](figures/versions_terms.png)

| | Stock v2 | v1 | **v2 (latest)** |
|---|---|---|---|
| Released | | 2026-10-15 | 2026-10-15 |
| Code-switching training audio | | 77 min | 120 min |
| Code-switching WER | 9.9% | 5.0% | **4.8%** |
| … phone recordings | 9.4% | 4.7% | **4.3%** |
| … desktop-mic recordings (30 clips) | 13.8% | **7.1%** | 8.6% |
| Hebrew terms seen in training, correct | 38% | 67% | **75%** |
| Hebrew terms never seen in training, correct | 29% | **52%** | 50% |
| Speaker's plain English WER | 2.7% | 2.5% | **2.4%** |
| LibriSpeech test-clean WER | 1.2% | 1.4% | **1.1%** |
| Long-form WER | 7.8% | 4.6% | **4.5%** |
| Pinned files | | [Q8_0](https://huggingface.co/danielrosehill/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching/resolve/ebc0e7aff1/gguf/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching-Q8_0.gguf) · [Q4_K_M](https://huggingface.co/danielrosehill/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching/resolve/ebc0e7aff1/gguf/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching-Q4_K_M.gguf) · [.nemo](https://huggingface.co/danielrosehill/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching/resolve/ebc0e7aff1/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching.nemo) | [Q8_0](https://huggingface.co/danielrosehill/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching/resolve/e1541065f8/gguf/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching-Q8_0.gguf) · [Q4_K_M](https://huggingface.co/danielrosehill/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching/resolve/e1541065f8/gguf/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching-Q4_K_M.gguf) · [.nemo](https://huggingface.co/danielrosehill/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching/resolve/e1541065f8/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching.nemo) |

**What v2 changed:** the extra 43 minutes of audio made the model better at Hebrew words it
has recordings of (67% → 75%) and slightly better on phone dictation. Words it has never
heard did not improve (52% vs 50% is a 3-hit difference out of 113: noise). The older
desktop-mic clips got a little worse; that is 30 clips of audio the model is not used on.
Full per-utterance results: `evals/r2-*.json` in the [model repo](https://huggingface.co/danielrosehill/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching/tree/main/evals).

### Data so far (2026-10-15, revision used for v2)

Code-switching takes, from the `metadata.jsonl` files on Hugging Face:

| Split | Clips | Audio | Of which recorded on the phone |
|---|---|---|---|
| train | 1,248 | 120 min | 88 min |
| test | 121 | 14 min | |

The rest came from the earlier desktop-mic round. The same split has 26 min of the speaker's
own monolingual English (29 min), but only 6 min of it is plain
English; the rest is tech and names sentences. So plain English is now a recording
priority. 529 distinct Hebrew terms appear in
train, but most only once, so recording is now weighted toward terms with only one or two
takes.

## In this repo

| Path | What |
|---|---|
| [`scripts/split_subsets.py`](scripts/split_subsets.py) | Builds category subsets (code-switching only, tech only, or any other category) from the main dataset, with the same layout, ids and train/test split. This is how the code-switching and tech datasets are derived. `--metadata-only` counts rows and minutes without downloading audio. |
| [`sentences/`](sentences/) | The full prompt bank the speaker reads from: `sentences.jsonl` (all 5,667 prompts, with categories, target Hebrew terms, split and source) and `code-switching.csv` (the 2,745 code-switching prompts). Licences per source are in `manifest.json`; most sentences were written by an LLM for this project and are CC-BY-4.0. |

## Design decisions

- **v2, not v3.** In the speaker's own use, v2 was more accurate than v3 for English
  dictation. v3 adds 25 languages and gives up some English accuracy.
- **Recorded on the phone that will run the model**: same microphone, rooms and posture as
  real dictation.
- **One romanized spelling per Hebrew word**, from the Hebrew-Latin-Token-Classifier
  lexicon. Variant spellings are rewritten to the canonical one, and terms are matched by
  word boundary, never by substring.
- **Transcripts are punctuated and cased**, matching v2's output style. Hebrew proper nouns
  are capitalised (Yerushalayim, Bituach Leumi).
- **The evaluation split is term-disjoint.** Held-out Hebrew terms appear only in test, so
  evaluation measures generalisation to unseen words, not memorised sentences. Per-term
  error is scored only on the held-out terms.
- **Every take is reviewed on the phone** (play, retake, delete or save) before it is
  published.

## Log

Newest first. One line per milestone.

- **2026-10-15**: v2 published (120 min of code-switching): code-switching WER 9.9% → 4.8% and unseen Hebrew terms 29% → 50% against stock v2, no English regression. HF now lists it as a fine-tune of v2.
- **2026-10-15**: Next retrain (v2) set for 120 min of code-switching training audio; 108 min
  so far (90%). Subset script and sentence bank published here; model card has a roadmap.
- **2026-10-15**: Demo Space live. Published transcripts normalised: 10 rows fixed,
  including a spelling-rewrite bug that turned "more" into "moreh". 301 missing Israeli-life
  terms found by a gap review and 868 sentences written for them. Recording now favours
  the words stock v2 gets wrong.
- **2026-10-15**: Baseline measured and first fine-tune published. Unseen Hebrew terms
  correct went from 30% to 55%, code-switching WER from 9.5% to 4.5%, with no English
  regression.
- **2026-10-15**: Training mix set from the code-switching literature: about 70%
  code-switching and 30% monolingual English.
- **2026-10-15**: Scope narrowed to code-switching; tech vocabulary dropped. Repo renamed from `Parakeet-V2-Personal-Finetune-Lifecycle`.
- **2026-10-15**: First data check: enough for a pilot. A capture-app button to record more
  sentences for a chosen term.
- **2026-10-14**: Code-switching subset dataset and its browser Space.
- **2026-10-14**: Capture app live; main dataset created and receiving takes.
- **2026-10-14**: Project planned.
