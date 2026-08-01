# EcoSort Edge — Slice 00 Project Charter

Status: Slice 00 complete; implementation has not started.

## What we are building

EcoSort Edge is a lightweight litter-detection and environmental-auditing prototype. Given an image, webcam feed, or recorded video, it will produce litter bounding boxes, a coarse waste-class prediction, confidence, processing speed, and optional low-confidence review/session summaries.

The project is an empirical study of robustness and deployment trade-offs. The central question is not merely whether a detector can find trash, but how it behaves when labels are sparse, objects are small or occluded, capture conditions change, and the model must run efficiently.

## Research questions and hypotheses

| ID | Question | Hypothesis to test |
|---|---|---|
| RQ1 | How well does a lightweight detector fine-tuned on TACO generalize to a small independent litter set? | External performance will drop, especially for small or visually unusual objects. |
| RQ2 | Does a smaller material-oriented taxonomy improve reliable detection for rare classes? | Coarse classes may be easier to learn, but they lose semantic detail. |
| RQ3 | Which intervention matters most: transfer learning, augmentation, resolution, or class rebalancing? | Pretraining will matter substantially; the other effects must be measured one at a time. |
| RQ4 | What accuracy–latency–model-size trade-off is available on GPU and CPU? | Faster/smaller settings will give up some accuracy, with the cost varying by object scale. |
| RQ5 | Can a confidence-and-review policy reduce dangerous false positives without hiding too many useful detections? | A validation-selected review threshold can trade coverage for higher precision, but confidence may be poorly calibrated externally. |

These are hypotheses, not conclusions. Results will be written only after the corresponding experiments and evaluations are complete.

## System boundary

### In scope

- TACO data acquisition, provenance checks, and deterministic annotation conversion.
- A documented coarse-label mapping.
- Leakage-aware train/validation/test splits.
- One small Ultralytics YOLO detector family.
- Internal and frozen external evaluation.
- Error analysis, controlled ablations, uncertainty/review behavior, and GPU/CPU efficiency measurement.
- An image/video demo that exposes the measured behavior.

### Explicitly out of scope

- Municipal operational decision-making.
- Automatic recyclability or material-certification decisions.
- Autonomous robot control.
- City-wide reliability claims.
- A large tournament of unrelated detector architectures.
- Automatic tracking or deduplication of objects across video frames.

Appearance does not always reveal material. Without tracking, the same object may be counted more than once in a video. A small TACO-plus-local test design cannot establish generalization beyond the evaluated data.

## Experiment map

| Experiment | Controlled change | Evidence question |
|---|---|---|
| E0 | No TACO fine-tuning | How transferable are generic pretrained labels? |
| E1 | Task-specific fine-tuning with coarse labels | What is the basic value of training on the task? |
| E2 | Augmentation off/on | Does augmentation improve robustness? |
| E3 | Input resolution | What is the small-object accuracy/latency trade-off? |
| E4 | Fine versus coarse taxonomy | Does label consolidation improve learnability? |
| E5 | Validation-selected confidence threshold | What review/coverage/precision trade-off is useful? |

Class rebalancing is a separate evidence-gated comparison. It will not be silently mixed into E1 or another experiment.

## Slice 00 exit gate

Before moving to Slice 01, I should be able to explain the project in about one minute, name at least three non-claims, and connect each research question to measurable evidence. The next slice will create the environment foundation, but it will not begin until you tell me what you want me to know before creating a Conda environment.
