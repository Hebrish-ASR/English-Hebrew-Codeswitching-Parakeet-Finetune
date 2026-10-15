# Parakeet-V2-Personal-Finetune-Lifecycle

Public tracker for a personal fine-tune of
[`nvidia/parakeet-tdt-0.6b-v2`](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v2): speech
recognition adapted to one speaker's voice, for dictation on an Android phone. This repo
records where the project stands and links to everything it publishes: datasets, tools and,
once it is released, the model. The working code lives in a separate private repository.

**Status (2026-10-15): collecting data.** No model has been trained yet.

## What the fine-tune is for

The speaker is an English speaker living in Jerusalem who dictates emails, messages and
instructions to AI coding agents. Stock Parakeet v2 handles general English well. It
struggles with:

| Target | Can read-aloud fine-tuning fix it? |
|---|---|
| Niche **tech vocabulary** (tools, self-hosting, AI) | Yes. This is the main target. |
| **Hebrew words inside English** ("pick up bamba from the makolet") | Yes, if each Hebrew word always has one romanized spelling |
| General accuracy on this speaker's voice | Yes. This is speaker adaptation. |
| **Homophones** | Partly. The sentences have to give the context that settles the spelling. |
| Disfluency removal, paragraph formatting | No. These are out of scope; post-processing handles them. |

## Links

| What | Link | Status |
|---|---|---|
| Base model | [`nvidia/parakeet-tdt-0.6b-v2`](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v2) | Upstream |
| **Fine-tuned model** | Not released yet | Pending. The base model's licence has to be checked before the weights are published. |
| **Main dataset**: every take recorded on the phone | [`danielrosehill/Read-Aloud-Voice-Sentences`](https://huggingface.co/datasets/danielrosehill/Read-Aloud-Voice-Sentences) | Live, growing |
| Subset: English-Hebrew code-switching | [`danielrosehill/English-Hebrew-Codeswitching-Sentences`](https://huggingface.co/datasets/danielrosehill/English-Hebrew-Codeswitching-Sentences) | Live, synced on every push |
| Subset: tech vocabulary | [`danielrosehill/Tech-Sentences`](https://huggingface.co/datasets/danielrosehill/Tech-Sentences) | Live, synced on every push |
| Browser for the code-switching data | [Space: `English-Hebrew-Codeswitching-Browser`](https://huggingface.co/spaces/danielrosehill/English-Hebrew-Codeswitching-Browser) | Live |
| Earlier round: code-switched recordings (desktop mic) | [`danielrosehill/English-Hebrew-Mixed-Sentences`](https://huggingface.co/datasets/danielrosehill/English-Hebrew-Mixed-Sentences) | Imported into the main dataset |
| Earlier round: tech sentences (desktop mic) | [`danielrosehill/Tech-Sentences-For-ASR-Training`](https://huggingface.co/datasets/danielrosehill/Tech-Sentences-For-ASR-Training) | Source of sentences |
| **Hebrew-Latin token classifier**: detects Hebrew words written in Latin letters inside English | [GitHub: `Hebrew-Latin-Token-Classifier`](https://github.com/danielrosehill/Hebrew-Latin-Token-Classifier) | Its lexicon sets the canonical romanized spellings used in every transcript here |
| Span review tool for the classifier | [Space: `hebrew-latin-span-review`](https://huggingface.co/spaces/danielrosehill/hebrew-latin-span-review) | Live |

## Lifecycle

| Stage | State | Notes |
|---|---|---|
| 1. Plan | Done, 2026-10-14 | Read-aloud sentences recorded on the target phone, NeMo fine-tune, on-device export |
| 2. Capture app | Done, 2026-10-14 | A phone web app in the style of Common Voice: read a sentence, record it, review, next. Takes are pushed to Hugging Face in batches. |
| 3. Data collection | **In progress** | See "Data so far" |
| 4. Baseline | Not started | Stock v2 scored on the held-out test split, in the same int8 runtime the phone uses |
| 5. Pilot fine-tune | Not started | Checks the pipeline end to end and whether per-term error moves at all |
| 6. Full fine-tune | Not started | Target about 2–3 h of audio, with 20–30% plain English to guard against forgetting |
| 7. On-device export | Not started | `.nemo` → int8 → Android dictation app; evaluated after quantisation, not only in PyTorch |
| 8. Release | Not started | Weights and evaluation results, if the base model's licence allows |

### Data so far (2026-10-15)

From the `metadata.jsonl` files on Hugging Face:

| Split | Clips | Audio | Of which recorded on the phone |
|---|---|---|---|
| train | 1,123 | 1.8 h | 655 clips, 79 min |
| test | 109 | 13 min | 79 clips, 11 min |

Code-switching makes up most of it: 925 train clips, 82 min. Plain English was nearly
absent (19 clips), so 835 everyday-English sentences were added to the sentence bank on
2026-10-15.

## Design decisions

- **v2, not v3.** In the speaker's own use, v2 was more accurate than v3 for English
  dictation. v3 adds 25 languages and gives up some English accuracy.
- **Recorded on the phone that will run the model**: same microphone, rooms and posture as
  real dictation. Earlier rounds used a desktop microphone.
- **Hebrew words are romanized**, using one canonical spelling per word from the
  Hebrew-Latin-Token-Classifier lexicon. The v2 tokenizer has no Hebrew characters.
- **Transcripts are punctuated and cased**, matching v2's output style.
- **The evaluation split is term-disjoint.** Held-out Hebrew and tech terms appear only in
  test, so evaluation measures generalisation to unseen words, not memorised sentences.
  Per-term error is scored only on the held-out terms.
- **Every take is reviewed on the phone** (play, retake, delete or save) before it is
  published.

## Log

Newest first. One line per milestone.

- **2026-10-15**: First data check: enough for a pilot fine-tune. Plain-English sentences
  added; a capture-app button to record more sentences for a chosen term.
- **2026-10-14**: Subset datasets for code-switching and tech, plus a browser Space.
- **2026-10-14**: Capture app live; main dataset created and receiving takes.
- **2026-10-14**: Project planned.
