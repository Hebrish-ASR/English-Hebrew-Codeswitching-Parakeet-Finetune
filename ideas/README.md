# Ideas

Things we could do to improve the model that are not planned or built yet. Each idea says what it is,
why, roughly how, and what would show it worked. When an idea is picked up, move it into the
training docs or the recording app's Tasks, and delete it here.

Datasets stay atomic: one audio dataset per phenomenon, so any of them can be left out of a
training round (Daniel, 2026-10-20). Keep each first round small: about 100–200 clips and the
cheapest benchmark that answers the question (about US$0.50 a round).

## Noise augmentation during training (added 2026-10-20)

**What:** mix artificial background noise, room echo and phone-codec distortion into some
training clips while they load. No new recordings, and no stored noisy copies.

**Why:** most recordings are clean, close-mic desk takes. Daily use is phones in cars, kitchens
and streets.

**How (inferred, not tried here):**
- NeMo's `train_ds.augmentor` applies augmentations on the fly. Candidates:
  - `noise`: a manifest of noise files, min/max SNR and a probability;
  - `impulse`: room impulse responses;
  - `speed`: speed perturbation.
- Starting values: 30–50 % of clips, SNR 5–20 dB.
- Make it a setting for each training round, so a round can be run with and without it.
- Noise sources, all free to use (check each licence before use):
  - MUSAN: noise, music and babble; CC BY 4.0.
  - DEMAND: home, office and street; CC BY-SA.
  - WHAM!: café and restaurant ambience.
  - OpenSLR 28: room impulse responses; Apache 2.0.
- Phone and Bluetooth sound: re-encode through a low-bitrate codec (Opus or AMR) as an extra
  augmentation step.

**How to tell it worked:** score the round on the clean held-out set and on a noisy copy of it.
It is a win only if the noisy WER drops and the clean WER does not rise. Compare with the same
round run without augmentation.

**Related:** real recordings in noisy places (a "recording conditions" task, below) capture how
the speaker talks in noise (louder, more clipped), which synthetic noise cannot. The two
complement each other. Clips flagged *Baby noise* or *Significant background noise* in the
recording app are real-noise data already.

## More recording tasks (added 2026-10-20)

Not built yet; each would be its own task and dataset in the recording app:

- **Short utterances:** one to three words ("yes", "send it", a name alone). Parakeet is weakest
  when it has little context.
- **Spelled-out text:** email addresses, URLs, version numbers, codes like "A7B-42".
- **Recording conditions:** the same kind of prompts recorded in the car, outside, in the
  kitchen, at arm's length, or quietly.
- **Long-form:** paragraph-length takes without stopping, for punctuation, sentence boundaries,
  and the joins between the Android app's per-pause segments.
