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

[![Download v3 GGUF Q8_0 (730 MB)](https://img.shields.io/badge/⬇_Download_v3-GGUF_Q8__0_·_730_MB_·_recommended-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/danielrosehill/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching/resolve/main/gguf/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching-Q8_0.gguf)
[![Download v3 GGUF Q4_K_M (475 MB)](https://img.shields.io/badge/⬇_Download_v3-GGUF_Q4__K__M_·_475_MB-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/danielrosehill/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching/resolve/main/gguf/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching-Q4_K_M.gguf)
[![Get Offline Voice Input on Google Play](https://img.shields.io/badge/Android_app-Offline_Voice_Input-34A853?style=for-the-badge&logo=googleplay&logoColor=white)](https://play.google.com/store/apps/details?id=dev.notune.transcribe)
[![Codeswitch Voice APK (POC)](https://img.shields.io/badge/Android_APK-Codeswitch_Voice_(POC)-2E7D6B?style=for-the-badge&logo=android&logoColor=white)](https://github.com/danielrosehill/English-Hebrew-Codeswitching-Voice-Keyboard-Android/releases/latest)
[![Try the demo](https://img.shields.io/badge/Try_it-Demo_Space-FF9D00?style=for-the-badge&logo=huggingface&logoColor=white)](https://huggingface.co/spaces/danielrosehill/English-Hebrew-Codeswitching-Parakeet-Demo)
[![Model card](https://img.shields.io/badge/Model-.nemo_·_2.47_GB-555555?style=for-the-badge&logo=nvidia&logoColor=76B900)](https://huggingface.co/danielrosehill/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching)

### Which file should I download?

All links below are the **latest version, v3** (2026-10-18); they always point to the newest
release. Earlier versions, with permanent links, are under **Version history**.

| You want to… | Download | Run it with |
|---|---|---|
| **Dictate on an Android phone** | **[Q8_0 GGUF](https://huggingface.co/danielrosehill/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching/resolve/main/gguf/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching-Q8_0.gguf)** (730 MB) | [Offline Voice Input](https://play.google.com/store/apps/details?id=dev.notune.transcribe) |
| Dictate on an Android phone with little memory (≤ 4 GB RAM), or if Q8_0 is too slow | [Q4_K_M GGUF](https://huggingface.co/danielrosehill/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching/resolve/main/gguf/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching-Q4_K_M.gguf) (475 MB) | Offline Voice Input |
| **Dictate on a Linux desktop** | **[Q8_0 GGUF](https://huggingface.co/danielrosehill/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching/resolve/main/gguf/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching-Q8_0.gguf)** (730 MB) | [Handy](https://github.com/cjpais/Handy) |
| Transcribe in Python, on a GPU, or fine-tune further | [`.nemo`](https://huggingface.co/danielrosehill/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching/resolve/main/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching.nemo) (2.47 GB, full precision) | [NVIDIA NeMo](https://github.com/NVIDIA-NeMo/Speech) |

**If unsure, take Q8_0.** It is the closest to full accuracy that still runs on a phone, and
on desktop CPUs it was also *faster* than Q4_K_M: about 3× realtime against 1.4× on 8 cores.
On five held-out test clips, Q8_0 matched the `.nemo` word for word; Q4_K_M differed on one word (v3, 2026-10-18). Speed on phones has not
been measured yet. ONNX, sherpa-onnx and MLX builds are in their own repos (links below).

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
Q4_K_M differed on one word (v3, checked 2026-10-18).

**Own app (proof of concept, 2026-10-18):** [Codeswitch Voice](https://github.com/danielrosehill/English-Hebrew-Codeswitching-Voice-Keyboard-Android) is a small voice
keyboard for testing. It downloads the v3 sherpa-onnx int8 weights (about 660 MB, pinned to
one HF revision) and runs them on the phone through sherpa-onnx. It is meant as the
companion voice input for **HeliBoard**: HeliBoard's mic key opens it, and you are returned
to HeliBoard once the text is in. [APK download](https://github.com/danielrosehill/English-Hebrew-Codeswitching-Voice-Keyboard-Android/releases/latest). Not yet tested on a
phone.

**Mac (Apple Silicon):** the [MLX build](https://huggingface.co/danielrosehill/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching-mlx)
runs with `pip install parakeet-mlx` and
`parakeet-mlx audio.wav --model danielrosehill/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching-mlx`,
or with mlx-audio. On 10 held-out clips it scored the same WER as the `.nemo`.

**Linux:** [Handy](https://github.com/cjpais/Handy) loads the same GGUF. Copy it into
`~/.local/share/com.pais.handy/models/` with its own file name; a name that matches a stock
catalogue file is treated as the stock model.

**Status (2026-10-18): v3 published** (196 min of code-switching). Data collection continues toward v4 at 270 min.
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
or two Hebrew words per sentence). v1 to v3 all used about 30% English without a
comparison; v4 is planned to compare 70/30, 80/20, 90/10 and 100/0 code-switching /
English and keep the best on both test sets: held-out code-switching and general English.

Sources: [Liu et al. 2025](https://arxiv.org/abs/2509.24310),
[Shah et al. 2020](https://arxiv.org/abs/2006.00782),
[Pekarek Rosin & Siegert 2023](https://arxiv.org/abs/2307.07280),
[CS ASR systematic review 2025](https://arxiv.org/abs/2507.07741).

## Training data (v3)

Everything v3 was trained on, by dataset. The training job pins one revision of
`Read-Aloud-Voice-Sentences` (`b47310621f79`) and adds public English replay at train time.

| Dataset | Whose | What v3 used from it | Licence |
|---|---|---|---|
| [`Read-Aloud-Voice-Sentences`](https://huggingface.co/datasets/danielrosehill/Read-Aloud-Voice-Sentences) | Mine | **The training source.** 1,921 code-switching clips (196.1 min): 1,482 takes from the capture app, mostly on the phone (169.3 min), and 439 recordings imported from the desktop-mic round below (26.8 min). Plus 338 clips of my own monolingual English (42.9 min). | CC-BY-4.0 |
| [`English-Hebrew-Codeswitching-Sentences`](https://huggingface.co/datasets/danielrosehill/English-Hebrew-Codeswitching-Sentences) | Mine | The code-switching phone takes, published on their own. Same audio as above, not extra data. | CC-BY-4.0 |
| [`English-Hebrew-Mixed-Sentences`](https://huggingface.co/datasets/danielrosehill/English-Hebrew-Mixed-Sentences) | Mine | An earlier desktop-mic round (2025-11-17). 439 of its recordings are imported into `Read-Aloud-Voice-Sentences` with fixed transcripts, and counted there. | MIT |
| [LibriSpeech](https://huggingface.co/datasets/openslr/librispeech_asr) `train-clean-100` with [LibriSpeech-PC](https://www.openslr.org/145/) transcripts | Public | 28.1 min of English replay, so the model keeps general English. LibriSpeech-PC supplies the cased, punctuated transcripts. `test-clean` (200 utterances) is used only for evaluation. | CC-BY-4.0 |

Actual mix by duration: 73.4% code-switching, 16.1% own English, 10.5% replay. Evaluation
uses the held-out test split of `Read-Aloud-Voice-Sentences` (219 code-switching clips,
term-disjoint) and is never trained on.

## Links

| What | Link | Status |
|---|---|---|
| Base model | [`nvidia/parakeet-tdt-0.6b-v2`](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v2) | Upstream |
| **Fine-tuned model** | [`danielrosehill/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching`](https://huggingface.co/danielrosehill/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching) | v3, 2026-10-18: `.nemo` plus GGUF Q8_0 and Q4_K_M. CC-BY-4.0, like the base model. v1 and v2 are in the repo history. |
| Android app that loads it | [Offline Voice Input](https://play.google.com/store/apps/details?id=dev.notune.transcribe) ([source](https://github.com/notune/android_transcribe_app)) | Imports the GGUF; works as a voice keyboard and as the system voice input |
| Own POC voice keyboard (Android APK) | [GitHub: `English-Hebrew-Codeswitching-Voice-Keyboard-Android`](https://github.com/danielrosehill/English-Hebrew-Codeswitching-Voice-Keyboard-Android) | v0.1.0, 2026-10-18. sherpa-onnx int8 v3, companion IME for HeliBoard |
| **Training data**: code-switching takes | [`danielrosehill/English-Hebrew-Codeswitching-Sentences`](https://huggingface.co/datasets/danielrosehill/English-Hebrew-Codeswitching-Sentences) | Live, synced on every push |
| **Project page**: every variant, results charts and a blog | [Space: `English-Hebrew-Codeswitching-Parakeet`](https://huggingface.co/spaces/danielrosehill/English-Hebrew-Codeswitching-Parakeet) | Live, 2026-10-16. Also in the [HF collection](https://huggingface.co/collections/danielrosehill/parakeet-v2-english-hebrew-codeswitching-finetune-6ad26d79c70d28a49ed71c78) |
| **Demo**: stock v2 vs the fine-tune, side by side | [Space: `English-Hebrew-Codeswitching-Parakeet-Demo`](https://huggingface.co/spaces/danielrosehill/English-Hebrew-Codeswitching-Parakeet-Demo) | Live (ZeroGPU) |
| **Benchmark**: this model against stock Parakeet and Whisper on a frozen code-switching test set | [Space: `English-Hebrew-Codeswitching-ASR-Leaderboard`](https://huggingface.co/spaces/danielrosehill/English-Hebrew-Codeswitching-ASR-Leaderboard) ([test set](https://huggingface.co/datasets/danielrosehill/English-Hebrew-Codeswitching-ASR-Benchmark), [runner](https://github.com/danielrosehill/English-Hebrew-Codeswitching-ASR-Benchmark)) | Live, v1 (2026-10-15). Headline metric is Hebrew term recall |
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
| 6. Retrains | v3 done, 2026-10-18 | v2 at 120 min, v3 at 196 min (~27% English each). Next: v4 at 270 min, with the 70/80/90/100% code-switching comparison. |
| 7. On-device export | GGUF, ONNX, sherpa-onnx, MLX done | v3 exported 2026-10-18: Q8_0 identical to PyTorch on 5 test clips, Q4_K_M and sherpa-onnx int8 off by one word. Phone test pending. |
| 8. Release | v3 released, 2026-10-18 | The base model is CC-BY-4.0, so fine-tunes are published openly |

## Results

**v3** (run `r3-en30`, 2026-10-18) was trained from stock v2 on 196 min of code-switching,
43 min of the speaker's English and 28 min of LibriSpeech replay. It took 29 minutes on one
GPU. Both models were scored on the current test split (219 code-switching clips).

| Test set | Stock v2 | Fine-tune v3 |
|---|---|---|
| Code-switching, held-out test (WER) | 10.9% | **5.3%** |
| Hebrew terms **never seen in training**: share correct | 27% | **48%** |
| Hebrew terms seen in training: share correct | 29% | **66%** |
| Speaker's plain English (WER) | 3.5% | **2.9%** |
| LibriSpeech test-clean (WER) | 1.2% | **1.0%** |
| Long form, ~3-minute files (WER) | 9.0% | **5.0%** |

![Word error rate, stock v2 vs the fine-tune](figures/wer.png)

![Hebrew terms transcribed correctly, stock v2 vs the fine-tune](figures/terms.png)

Every version side by side, on the same test split, is under **Version history** below. On
the separate, frozen [public benchmark](https://huggingface.co/spaces/danielrosehill/English-Hebrew-Codeswitching-ASR-Leaderboard),
v3 is first at 67.4% Hebrew term recall (v2 65.7%, Whisper Large V3 45.9%, stock Parakeet
v2 32.6%).

WER here is lowercase with punctuation removed. English did not get worse. The jump on
unseen terms suggests the model learned how this speaker's Hebrew maps to the
romanization, not only the training words.

![How stock v2 handles the Hebrew terms in the training recordings](figures/baseline_terms.png)

The baseline also shows which words matter. Across 1,139 terms in the training recordings,
stock v2 gets 258 right every time: mostly names, well-known places and words that are
already English. It never gets 706 right: challah, cheshbonit, sabich, Motzei Shabbat,
osek patur, tachana merkazit. Recording concentrates on that second group.

### Version history

Every version is re-scored on the **same** test split as the newest one (revision
`b47310621f79`), so the rows below compare like with like. The download links at the top of
this page are always the latest version; the links in the last row stay pinned to each
version's files forever.

![Word error rate by version](figures/versions_wer.png)

![Hebrew terms transcribed correctly, by version](figures/versions_terms.png)

| | Stock v2 | v1 | v2 | **v3 (latest)** |
|---|---|---|---|---|
| Released | | 2026-10-15 | 2026-10-15 | 2026-10-18 |
| Code-switching training audio | | 77 min | 120 min | 196 min |
| Code-switching WER | 10.9% | 6.0% | 5.8% | **5.3%** |
| … phone recordings | 10.7% | 6.0% | 5.6% | **5.1%** |
| … desktop-mic recordings (30 clips) | 13.8% | **7.1%** | 8.6% | 8.6% |
| Hebrew terms seen in training, correct | 29% | 57% | 60% | **66%** |
| Hebrew terms never seen in training, correct | 27% | 47% | 47% | **48%** |
| Speaker's plain English WER | 3.5% | 3.2% | **2.6%** | 2.9% |
| LibriSpeech test-clean WER | 1.2% | 1.4% | 1.1% | **1.0%** |
| Long-form WER | 9.0% | 5.9% | 5.6% | **5.0%** |
| Pinned files | | [Q8_0](https://huggingface.co/danielrosehill/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching/resolve/ebc0e7aff1/gguf/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching-Q8_0.gguf) · [Q4_K_M](https://huggingface.co/danielrosehill/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching/resolve/ebc0e7aff1/gguf/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching-Q4_K_M.gguf) · [.nemo](https://huggingface.co/danielrosehill/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching/resolve/ebc0e7aff1/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching.nemo) | [Q8_0](https://huggingface.co/danielrosehill/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching/resolve/e1541065f8/gguf/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching-Q8_0.gguf) · [Q4_K_M](https://huggingface.co/danielrosehill/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching/resolve/e1541065f8/gguf/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching-Q4_K_M.gguf) · [.nemo](https://huggingface.co/danielrosehill/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching/resolve/e1541065f8/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching.nemo) | [Q8_0](https://huggingface.co/danielrosehill/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching/resolve/728e6f88d4/gguf/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching-Q8_0.gguf) · [Q4_K_M](https://huggingface.co/danielrosehill/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching/resolve/728e6f88d4/gguf/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching-Q4_K_M.gguf) · [.nemo](https://huggingface.co/danielrosehill/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching/resolve/728e6f88d4/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching.nemo) |

**What v3 changed:** 76 more minutes of code-switched audio lowered code-switching WER from
5.8% to 5.3% and long-form WER from 5.6% to 5.0%, and Hebrew words with recordings went from
60% to 66% correct. Words the model has never heard barely moved (47% → 48%, one hit out of
176). Three versions now show the same thing: more takes of a word help that word, but more
audio alone does not help new words. Full per-utterance results: `evals/r3-*.json` in the
[model repo](https://huggingface.co/danielrosehill/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching/tree/main/evals);
the scores are also in the model card's `model-index` metadata.

### Data so far (2026-10-18, revision used for v3)

Code-switching takes, from the `metadata.jsonl` files on Hugging Face:

| Split | Clips | Audio | Of which from the capture app |
|---|---|---|---|
| train | 1,921 | 196 min | 169 min |
| test | 219 | 25 min | |

The rest came from the earlier desktop-mic round. The same revision has 43 min of the
speaker's own monolingual English, 10 min of it plain English and the rest names, tech and
numbers sentences. 1,000 distinct Hebrew terms appear in the code-switching train rows; 715
of them have only one or two takes, so recording is weighted toward those.

## Open questions and ideas

On 2026-10-18 the speaker recorded an 18-minute voice note of open questions and ideas for
the project ([audio](voice-notes/2026-10-18-project-notes/voice-note.mp3), [transcript](voice-notes/2026-10-18-project-notes/transcript.md)). This section is what it
raises. Nothing here is settled.

**Data to collect**

- **Messier acoustic conditions.** Most takes so far were recorded at home, but real
  dictation happens elsewhere: in the street with traffic and construction drilling, in cafés,
  at the shuk, with a baby crying nearby. A few takes with a crying baby are already
  recorded. More takes outside the home are wanted, even with no new vocabulary in them.
- **More microphones.** Every capture-app take so far comes from one phone (OnePlus Nord 3
  5G). Desktop-microphone takes will follow once the desk is set up again after a move.
- **Pronunciation variants.** Where a Hebrew word has two common pronunciations, such as the
  Diaspora (Ashkenazi) and the Israeli *Rosh Hashanah*, takes are recorded in both, so that
  the model writes one spelling for either.
- **Other speakers, later.** All training takes are still the speaker's own. Wanted later:
  female voices; other English accents common in Israel (South African, Australian, British,
  American; an Irish accent is a small minority); and Sephardi as well as Ashkenazi
  pronunciations of Hebrew. A contributor login for the capture app could follow once the
  project has some momentum.
- **Vocabulary from other people's blind spots.** Ask dictation users from other walks of
  life, for example more religious friends, which words their tools always get wrong. Gaps
  being filled now: smaller towns, moshavim and kibbutzim, street names in Jerusalem and Tel
  Aviv, public figures, politicians and new party names.
- **TTS errors as a vocabulary signal.** When a text-to-speech voice mispronounces an
  Israeli name (seen with a new political party in the speaker's AI-generated podcast), the
  word is missing from common lexicons, so it is a candidate for the sentence bank.

**Tooling**

- **Tagging after the fact.** Recording conditions (noise, crying, speaker) are tagged on the
  phone, which is awkward and often skipped. Ideas: a web tool to correct the tags
  afterwards, and an audio classifier that learns from a few tagged clips (a child crying,
  say) and finds the untagged ones.

**Open questions**

1. **How many takes does a word need?** *Hafnaya* (a medical referral) comes up all the
   time. Are 6 sentences with it enough, or 12? Should take counts be weighted by how often a
   word is actually used, so that everyday words get more takes than once-a-year ones?
2. **Should the general fixes go into every fine-tune?** Numbers written as digits and
   homophones target general weaknesses of stock v2, not code-switching. Should those
   sentences join the code-switching and tech training mixes, or would they dilute them?
3. **Speech that is not the speaker's.** In a café or the street there are often other
   conversations nearby, in Israel frequently in several languages at once. Can a fine-tune
   learn to ignore them, from loudness for example, or does that need diarization or a
   separate target-speaker model? Not a code-switching target, but a real one.
4. **Language of origin.** Some words used in English in Israel are Yiddish rather than
   Hebrew (*mamish* beside the Hebrew *mamash*), and many Hebrew words come from other
   languages. For now they are not told apart: this is a dictation tool, and its users mix
   words from several languages of origin.

**Direction**

- **Separate, targeted fine-tunes** rather than one that covers everything: code-switching
  first (the core of the project), then tech vocabulary and accent, possibly a third for
  general fixes. Training a model on a domain it does not need risks overfitting and
  forgetting for no gain. The main dataset stays one growing clip library that each
  fine-tune draws its own mix from.
- **Slower, steady updates.** v1 to v3 were the proof of concept. From here, about 20 to
  30 minutes of recording a week, and daily use on the phone as the real test.
- **Use cases beyond dictation:** Israeli place names spoken into navigation apps (Waze) in
  the car, medical words for patients rather than doctors, notes to self.
- **Audience:** English speakers living in Israel who already dictate and notice that every
  model, Whisper included, fails on Hebrew words, rather than local-AI specialists. Once it
  holds up in daily use, share it with immigrant organisations such as Nefesh B'Nefesh.
- **Collaboration** with the Israeli Hebrew NLP community (for example Dicta), who work on
  Hebrew LLMs, TTS and ASR. First contact has been made.
- **Apple Silicon:** done, as the MLX build (2026-10-18).

## In this repo

| Path | What |
|---|---|
| [`scripts/split_subsets.py`](scripts/split_subsets.py) | Builds category subsets (code-switching only, tech only, or any other category) from the main dataset, with the same layout, ids and train/test split. This is how the code-switching and tech datasets are derived. `--metadata-only` counts rows and minutes without downloading audio. |
| [`voice-notes/`](voice-notes/) | The speaker's voice notes about the project, each with its audio and transcript. The 2026-10-18 note is the source of **Open questions and ideas**. |
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

- **2026-10-18**: Voice note of open questions and ideas ([audio and transcript](voice-notes/2026-10-18-project-notes/)), summarised under **Open questions and ideas**: messier recording conditions, more microphones and speakers, how many takes a word needs, and whether general fixes belong in every fine-tune.
- **2026-10-18**: v3 for Apple Silicon: [MLX build](https://huggingface.co/danielrosehill/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching-mlx) for parakeet-mlx and mlx-audio, the same WER as the `.nemo` on 10 held-out clips.
- **2026-10-18**: Sentence bank grows from 9,735 to 10,277 prompts: an everyday-vocabulary pack (home repairs, parenting and gan, work, renting, produce, army reserves, the missing Hebrew months), whole Hebrew reactions and fillers (legamrei, rak rega, ein li musag), and the bank's first short utterances of 2 to 4 words.
- **2026-10-18**: [Codeswitch Voice](https://github.com/danielrosehill/English-Hebrew-Codeswitching-Voice-Keyboard-Android) v0.1.0: a proof-of-concept Android voice keyboard (APK) that runs v3 on-device through sherpa-onnx, as the companion voice input for HeliBoard.
- **2026-10-18**: **v3 released** (run `r3-en30`, 196 min of code-switching): code-switching WER 5.3% (stock v2 10.9%, v2 5.8%), Hebrew terms with recordings 66% correct (v2 60%), no loss of English. GGUF, ONNX and sherpa-onnx exports refreshed; the model card now carries `model-index` eval metadata. First on the public benchmark at 67.4% term recall.
- **2026-10-17**: Sentence bank grows from 9,443 to 9,735 prompts with a medical pack: health-fund admin words, medical terms, hospitals and 58 Israeli drug trade names (Acamol-family, Moxypen, Lorivan…), 292 sentences. Published takes gain a `prompt_origin` column (manual / dataset / generated).
- **2026-10-17**: Sentence bank grows from 8,325 to 9,443 prompts with a tech pack of 377 terms (cloud-native projects, AI model families, developer tools and libraries), for a planned second fine-tune on tech vocabulary and accent. These sentences are English only, with no code-switching. Exported to `sentences/`.
- **2026-10-17**: Sentence bank grows from 7,697 to 8,325 prompts with a Jewish observance pack (kashrut and certification bodies, Shabbat, Daf Yomi and Torah study, prayer, holiday prep), weighted to everyday words rather than once-a-year ones. New subset dataset [`General-English-Sentences`](https://huggingface.co/datasets/danielrosehill/General-English-Sentences): plain English takes with no Hebrew, names or tech, for accent-only fine-tuning.
- **2026-10-16**: Project page Space live: links to every published format (.nemo, GGUF, ONNX, sherpa-onnx), interactive results charts and a blog, added to the HF collection.
- **2026-10-16**: Sentence bank grows from 5,752 to 7,697 prompts with five vocabulary packs: Jerusalem and Tel Aviv places, hospitals and health words, everyday code-switching gaps, second-tier towns, moshavim and kibbutzim, Israeli brands and acronyms (El Al, Arkia, Israir), and 2026 election parties, politicians and media names. Exported to `sentences/`.
- **2026-10-15**: Public benchmark released: a frozen code-switching test set, runner and leaderboard Space. It scores this fine-tune against stock Parakeet and Whisper models.
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
