# EcoSort Edge — Learning-First Build Plan

This is the canonical plan for building **Project 1 — EcoSort Edge** from `AI_QML_Project_Handbook.docx`. It deliberately excludes every other project in the handbook.

The project will be built in **25 small slices, numbered 00–24**. We will complete only one slice at a time. A slice is complete only after its code or evidence works **and** you can explain the important ideas in it.

## 1. Technical summary and project boundary

EcoSort Edge will be a lightweight litter-detection and environmental-auditing prototype. It will accept an image, webcam feed, or recorded video and produce:

- litter bounding boxes;
- a coarse waste-class prediction;
- a confidence score;
- processing-speed information;
- low-confidence items marked for human review; and
- an optional session summary.

The research question is broader than “can YOLO detect trash?” We will test how a small pretrained detector behaves after TACO fine-tuning, how it generalizes to independently collected images, which controlled interventions help, how uncertainty can drive review, and what accuracy–speed–size trade-off is available on GPU and CPU.

The project will **not** claim to be a municipal decision system, a recycling oracle, or an autonomous robot controller. Appearance alone cannot always reveal material, video detections may double-count objects without tracking, and a small external test set cannot prove city-wide reliability.

## 2. Our working agreement

These rules override the temptation to build ahead:

1. **One slice per implementation cycle.** When you ask for Slice NN, I will implement only that slice and the smallest prerequisite correction needed for it.
2. **Explain before and after.** Before editing, I will explain the slice’s purpose, inputs, outputs, and new concepts. After editing, I will walk through every meaningful file and command.
3. **No hidden scaffolding.** We will not prebuild later pipelines, demo screens, abstractions, or utilities “for convenience.” A file appears when its slice needs it.
4. **Visible proof.** Every slice ends with a test, visual check, saved evidence, or reproducible command. “The code ran once” is not enough.
5. **Understanding gate.** We stop after the slice. You may ask anything, request another example, change code yourself, or ask for a small exercise. We advance only when you explicitly say to proceed.
6. **Teach-back over memorization.** You do not need to memorize syntax, but you should be able to explain what the slice does, why it exists, what can fail, and how we verified it.
7. **One scientific change at a time.** Experiments will reuse the same split, seed policy, model family, and evaluator unless the experiment explicitly changes one of them.
8. **No test-set tuning.** The internal test set and sealed external set will never choose training settings, thresholds, or checkpoints.
9. **Reproducibility as we go.** Each slice records commands, configuration, versions, seeds, and outputs needed to reproduce its evidence.
10. **Honest claims only.** The README, model card, demo, report, and verbal explanation must match the measured evidence.

### Standard handoff for every slice

At the end of each slice I will provide:

- what changed and why;
- the exact command(s) to run;
- what output you should expect;
- a file-by-file explanation;
- the proof that the slice works;
- common failure modes;
- two or three teach-back questions; and
- the explicit message: **“Slice NN is complete; I will not start Slice NN+1 until you ask.”**

If your answer to a teach-back question exposes a gap, that is useful: we stay on the same slice and clarify it.

## 3. Provisional technical choices

These choices keep the project focused but are not silently final. We will inspect the machine and data before pinning exact versions or variants.

- Python, PyTorch, and one small Ultralytics YOLO detector family.
- TACO as the labeled source dataset, retaining original annotation provenance.
- Versioned YAML configuration for taxonomy, data splits, training, evaluation, and inference.
- `pytest` for focused correctness checks.
- OpenCV for image/video input where appropriate.
- A simple local demo framework chosen only when we reach the demo slices.

We will not compare many unrelated detector architectures. The detector family stays fixed so the experiments answer meaningful questions rather than becoming a model tournament.

## 4. The 25 build slices

### Phase A — Define the experiment and learn the primitives

#### Slice 00 — Freeze the learning contract and research map

**Purpose:** Make sure we can explain what we are building before code makes the project look more complete than it is.

**We will create:**

- a concise project charter derived from this plan;
- the five research questions and their hypotheses;
- the input/output boundary and explicit non-claims;
- an experiment-ID map for E0–E5; and
- a status log template used by every later slice.

**You will understand:** Why this is an empirical robustness/deployment study rather than a generic object-detection demo; the difference between a hypothesis and a result; and why system boundaries matter.

**Proof / exit gate:** You can describe the project in roughly one minute, name at least three non-claims, and explain which evidence would answer each research question. No training code exists yet.

#### Slice 01 — Repository, Python environment, and one-command smoke test

**Purpose:** Establish a small, inspectable foundation without generating the final repository all at once.

**We will create:**

- the minimal directories needed now;
- dependency and environment metadata;
- a tiny importable Python package or module;
- a command that reports Python, PyTorch, CUDA, GPU, and key package versions; and
- one trivial automated test.

**You will understand:** Virtual environments, dependencies, modules, imports, CPU versus CUDA, why package versions are evidence, and what a smoke test proves.

**Proof / exit gate:** A clean shell can activate the environment, run the diagnostic command, and pass the test. You can explain every top-level file created in this slice.

#### Slice 02 — Image arrays and tensor transformations

**Purpose:** Learn the data representation that every later detector step relies on.

**We will create:** A small learning script that loads one local sample image, inspects height/width/channel order, converts it to a tensor, resizes it, normalizes it, and saves a clearly labeled comparison.

**You will understand:** Pixels, RGB channels, array/tensor shapes, integer versus floating-point ranges, resizing, normalization, batching, and why careless transformations can corrupt boxes or colors.

**Proof / exit gate:** You can predict the shape and value range after each transformation and deliberately diagnose one introduced shape or channel-order error.

#### Slice 03 — Object-detection concepts in a visual sandbox

**Purpose:** Make detector outputs understandable before using a pretrained detector.

**We will create:** A tiny visual sandbox using hand-authored boxes to calculate and display intersection over union (IoU), confidence filtering, and non-maximum suppression (NMS).

**You will understand:** Bounding-box coordinate formats, class labels, confidence, true/false positives, IoU, duplicate detections, NMS, and why classification accuracy is not a detection metric.

**Proof / exit gate:** Given two boxes and thresholds, you can explain whether they overlap enough to match or suppress and how changing a threshold alters the output.

### Phase B — Build a trustworthy data foundation

#### Slice 04 — Data governance and the sealed external-set protocol

**Purpose:** Protect the future generalization test before any model result can influence data collection or tuning.

**We will create:**

- rules for collecting roughly 100–200 personal external images;
- a separate negative-image checklist;
- privacy and safety rules covering faces, number plates, precise location metadata, and unsafe collection;
- a manifest format for image IDs and non-sensitive capture context; and
- a sealed-set rule explaining when files may be viewed or evaluated.

**You will understand:** Internal versus external evaluation, domain shift, negative controls, test-set contamination, and why repeated inspection turns a test set into a validation set.

**Proof / exit gate:** The collection checklist and manifest validate on a few dummy entries. Real collection may continue in parallel, but no model is evaluated on it yet.

#### Slice 05 — Acquire TACO and verify raw-data integrity

**Purpose:** Download data reproducibly and distinguish immutable source data from generated project data.

**We will create:** A documented official-toolkit download procedure, raw-data location rules, a manifest/check script, and a short integrity report covering missing or corrupted images and annotation/image references.

**You will understand:** COCO-format structure at a high level, images versus annotations, category IDs, provenance, checksums/manifests, and why raw data should not be edited in place.

**Proof / exit gate:** A repeatable validation command reports the same dataset counts and clearly fails on one intentionally broken fixture.

#### Slice 06 — Explore and audit at least 50 annotations

**Purpose:** Learn what the detector will actually see before choosing labels or training settings.

**We will create:**

- an annotation explorer;
- a saved grid or browsing output covering at least 50 annotations;
- class-frequency and object-size summaries; and
- a short audit of occlusion, tiny objects, confusing backgrounds, and annotation problems.

**You will understand:** Long-tail class imbalance, bounding-box area, small/medium/large objects, annotation quality, and how visual inspection complements statistics.

**Proof / exit gate:** We can trace plotted boxes back to their source annotations, and you can name the most important data risks based on evidence rather than assumption.

#### Slice 07 — Design and test the coarse waste taxonomy

**Purpose:** Turn TACO’s sparse fine-grained labels into a documented, testable learning target.

**We will create:** A versioned mapping configuration, a validator that catches missing/duplicate/invalid mappings, tests for representative categories, and before/after distribution summaries.

**You will understand:** Fine versus coarse taxonomy, semantic trade-offs, rare classes, why label consolidation may improve learnability, and why mappings must never change silently.

**Proof / exit gate:** Every included source category maps exactly once, excluded categories are explicit, and you can defend the proposed classes without claiming that appearance guarantees recyclability or material.

#### Slice 08 — Deterministic COCO-to-detector conversion

**Purpose:** Convert annotations without mixing conversion logic with splitting or training.

**We will create:** A reusable conversion command, generated detector labels, a conversion summary, focused tests, and a round-trip visual check on selected images.

**You will understand:** COCO box coordinates versus normalized detector coordinates, class-index remapping, clipping/invalid boxes, deterministic output, and why conversion errors can look like model failures.

**Proof / exit gate:** Re-running conversion produces identical outputs; tests cover a known box, an invalid box, and a mapping case; plotted converted boxes align with the originals.

#### Slice 09 — Leakage-aware train/validation/test splits

**Purpose:** Create fixed split manifests that support honest model selection and final evaluation.

**We will create:** A split generator, grouping/stratification rules based on available metadata, versioned split files, distribution summaries, and integrity tests preventing overlap.

**You will understand:** Training, validation, and test roles; data leakage; grouping by source/capture context; imperfect stratification; seeds; and why the test split cannot choose settings.

**Proof / exit gate:** The same seed reproduces the same split, no image/group crosses boundaries, all eligible images appear exactly once, and limitations are documented.

### Phase C — Establish baselines and a reproducible training/evaluation loop

#### Slice 10 — E0: unmodified pretrained-model baseline

**Purpose:** Establish what generic pretrained labels can and cannot do before task-specific fine-tuning.

**We will create:** A small inference command, saved raw predictions, and a curated sample of successes and failures. This is E0, not the final model.

**You will understand:** Model weights, inference mode, preprocessing, predicted boxes/classes/confidences, and why a generic model’s label space does not directly solve TACO.

**Proof / exit gate:** The same inputs produce saved, inspectable predictions, and you can explain why E0 is a baseline rather than a fair final detector.

#### Slice 11 — Training mechanics through a tiny overfit experiment

**Purpose:** Understand the training loop before paying for a full run.

**We will create:** A minimal training configuration for a tiny subset, fixed seed handling, output/checkpoint locations, and plots or logs for a short overfit/smoke run.

**You will understand:** Transfer learning, batches, epochs, loss, gradients, optimizer steps, train/eval mode, checkpoints, GPU memory, and why deliberately overfitting a tiny set is a pipeline diagnostic.

**Proof / exit gate:** The tiny run completes, saves a checkpoint, and shows the expected learning behavior. You can narrate one training iteration in the correct order.

#### Slice 12 — E1: reproducible coarse-label fine-tuning baseline

**Purpose:** Train the first serious task-specific detector while keeping settings simple and recorded.

**We will create:** The main baseline training configuration and entry command, experiment metadata, curves, best-checkpoint selection, and hardware/runtime records.

**You will understand:** What is inherited from pretraining, which settings are fixed, how validation selects a checkpoint, and why test/external results do not influence training.

**Proof / exit gate:** E1 can be reproduced from its config and split manifests, its best checkpoint is selected only by validation evidence, and the run record contains the seed and package/hardware context.

#### Slice 13 — Build the internal evaluation engine

**Purpose:** Separate measurement from training so every experiment is judged the same way.

**We will create:** A frozen-checkpoint evaluation command that reports mAP@0.5, mAP@0.5:0.95, precision/recall at stated thresholds, per-class results when sample sizes permit, and small/medium/large object breakdowns.

**You will understand:** Matching predictions to ground truth, precision–recall behavior, average precision, mAP thresholds, macro versus per-class interpretation, object-size breakdowns, and the limits of small samples.

**Proof / exit gate:** The evaluator passes hand-checkable metric fixtures and evaluates E1 without changing its weights or choosing settings from test results.

#### Slice 14 — Frozen external and negative-set evaluation

**Purpose:** Answer the main generalization question using settings frozen before opening the sealed data.

**We will create:** Validated external/negative manifests, a one-time evaluation protocol, internal-versus-external summary, false positives per negative image, and a permanent record of exactly which model and threshold were used.

**You will understand:** Domain shift, why the same threshold must be used, aggregate versus unstable per-class estimates, uncertainty intervals when feasible, and why negative images measure a different failure mode.

**Proof / exit gate:** The frozen model is evaluated without retraining or threshold changes, and the result clearly separates internal, external, and negative-set evidence.

#### Slice 15 — Structured qualitative error analysis

**Purpose:** Turn failures into testable explanations rather than a gallery of embarrassing examples.

**We will create:** An error taxonomy and reviewed grids for small-object misses, occlusion, material/class confusion, localization errors, background false alarms, and threshold-sensitive cases.

**You will understand:** False-positive and false-negative subtypes, diagnosis versus speculation, sample selection bias in qualitative grids, and how error evidence motivates an intervention.

**Proof / exit gate:** Each displayed case links to saved prediction/ground-truth data, category counts are reported, and we identify interventions only where evidence supports them.

### Phase D — Run controlled experiments one factor at a time

#### Slice 16 — E2: augmentation ablation

**Purpose:** Test whether augmentation improves robustness rather than assuming that more augmentation is better.

**We will create:** Paired augmentation-off/on configs with all other factors fixed, transformation visualizations, and an internal/external comparison.

**You will understand:** Train-only augmentation, label-safe geometric transforms, distribution shift, paired comparisons, and how unrealistic augmentation can hurt.

**Proof / exit gate:** The comparison changes only augmentation, uses the shared evaluator, and ends with a measured conclusion or an explicit inconclusive result.

#### Slice 17 — E3: image-resolution trade-off

**Purpose:** Test the expected small-object accuracy versus latency cost.

**We will create:** Paired resolution configs, detection-quality and object-size results, and preliminary timing measured with the same procedure.

**You will understand:** Input resizing, receptive-field intuition, small-object information loss, compute scaling, and why one resolution may not dominate on every metric.

**Proof / exit gate:** Only input resolution changes, and the result reports both quality and efficiency rather than selecting whichever metric looks best.

#### Slice 18 — E4: fine-versus-coarse taxonomy comparison

**Purpose:** Directly test whether label consolidation improves learnability under limited data.

**We will create:** A carefully matched fine-label run, an evaluation plan that makes unlike label spaces interpretable, distribution context, and a comparison that explicitly discusses rare-class instability.

**You will understand:** Why headline metrics across different taxonomies can mislead, how to construct a fair comparison, and what “better” means when semantic detail changes.

**Proof / exit gate:** The comparison uses documented matching rules and supports a bounded conclusion about learnability—not a claim that coarse labels are universally superior.

#### Slice 19 — Class rebalancing decision and controlled test

**Purpose:** Answer the class-rebalancing part of RQ3 only if the audit and errors justify it.

**We will create:** A written go/no-go decision. If justified, one controlled weighting/sampling intervention and its comparison; if not, evidence explaining why the experiment would add noise rather than insight.

**You will understand:** Class imbalance versus data scarcity, loss weighting/sampling trade-offs, overfitting rare examples, and why “not run” can be a rigorous experimental decision.

**Proof / exit gate:** Either one factor changes and is evaluated consistently, or the omission is explicitly justified in the experiment log.

#### Slice 20 — E5: confidence threshold and human-review policy

**Purpose:** Convert uncertainty into transparent system behavior instead of treating confidence as correctness.

**We will create:** Confidence distributions for correct/incorrect predictions, a validation-selected threshold analysis, coverage/precision or coverage/risk summaries, and the low-confidence review rule. Optional calibration error is included only if we can define and test it responsibly.

**You will understand:** Confidence versus probability of correctness, calibration, threshold selection, abstention/review, coverage, and why the test/external set cannot choose the threshold.

**Proof / exit gate:** The policy is selected on validation data, then reported unchanged on internal test and external data; its benefit and cost are both visible.

#### Slice 21 — Multi-seed confirmation of the compact final comparison

**Purpose:** Check whether the most important conclusions survive randomness.

**We will create:** A compact, affordable final matrix using at least three seeds where feasible, paired aggregation, mean/standard deviation summaries, and an explicit limitation if compute prevents the full plan.

**You will understand:** Sources of training randomness, paired seeds, variance, mean and standard deviation, practical versus noisy differences, and why one lucky run is weak evidence.

**Proof / exit gate:** Seed pairing and configs are auditable, failed runs are not silently dropped, and final claims reflect variability.

### Phase E — Measure deployment behavior and build the user-facing prototype

#### Slice 22 — Reproducible GPU/CPU efficiency benchmark

**Purpose:** Answer the accuracy–latency–model-size question with a fair timing method.

**We will create:** A benchmark command with warm-up, representative batch size, repeated trials, GPU synchronization where needed, median and 95th-percentile latency, frames per second, parameter count, and model-file size. A smaller resolution or supported export is compared only under the same conditions.

**You will understand:** Warm-up, synchronization, throughput versus latency, median versus tail latency, CPU/GPU differences, batch-size effects, and why one convenient timing is misleading.

**Proof / exit gate:** Repeated runs are reasonably stable, all compared variants share the procedure, and hardware/software context is saved with results.

#### Slice 23 — Image inference demo with uncertainty review

**Purpose:** Expose the frozen pipeline through the smallest useful interface before adding streaming/video complexity.

**We will create:** An image-upload inference screen showing boxes, coarse class, confidence, speed, and a low-confidence review panel, plus a compact export of results.

**You will understand:** The path from UI input to preprocessing, model inference, postprocessing, review policy, visualization, and export; and the difference between UI state and model state.

**Proof / exit gate:** Unseen images and a no-litter negative image work end to end, low-confidence behavior is visible, and exported results can be traced back to displayed detections.

#### Slice 24 — Video/session auditing and final scientific handoff

**Purpose:** Add the final input mode, then make the whole project reproducible and defensible without hiding unfinished work.

**We will create:**

- recorded-video and optional webcam inference;
- session counts and low-confidence review items;
- an explicit warning about double-counting without tracking;
- final clean-environment tests for conversion, splits, metrics, and inference;
- the experiment/result table containing E0, E1, at least two controlled ablations, external evaluation, and efficiency;
- README, model card, limitations, reproducibility commands, and a short research report; and
- a five-minute professor-facing explanation starting with the demo, then domain shift, the most informative ablation, three failure categories, and the latency trade-off.

**You will understand:** Frame-wise inference, session aggregation, where tracking would fit and why it is out of scope, reproducibility from a clean environment, evidence consistency, and how to defend limitations.

**Proof / exit gate:** The demo works on unseen media; required commands run from a clean environment; report, README, model card, and verbal explanation agree; all five research questions receive evidence-backed answers or explicit limitations; and no claim exceeds the evaluated data.

## 5. Experiment map

| Experiment | Built in | One changed factor | Main question |
|---|---:|---|---|
| E0 | Slice 10 | No TACO fine-tuning | How poorly do generic labels transfer? |
| E1 | Slice 12 | Task-specific fine-tuning enabled | What is the basic value of fine-tuning? |
| E2 | Slice 16 | Augmentation off/on | Does augmentation improve external robustness? |
| E3 | Slice 17 | Input resolution | What is the small-object accuracy/latency trade-off? |
| E4 | Slice 18 | Fine versus coarse taxonomy | Does label consolidation improve learnability? |
| E5 | Slice 20 | Confidence threshold | What coverage/precision trade-off supports review? |

Class rebalancing is a separate evidence-gated comparison in Slice 19, not something silently mixed into E1 or E2.

## 6. Research-question traceability

| Research question | Primary evidence slices |
|---|---|
| RQ1: Internal-to-external generalization | 12–15 and 21 |
| RQ2: Fine versus coarse taxonomy | 07, 18, and 21 |
| RQ3: Transfer learning, augmentation, resolution, and rebalancing | 10–12 and 16–19 |
| RQ4: Accuracy–latency–size trade-off on GPU and CPU | 17, 21, and 22 |
| RQ5: Confidence-and-review policy | 14, 15, 20, and 23–24 |

## 7. Progress tracker

Only this status table should move ahead. Later-slice code should not appear early.

| Slice | Short name | Status |
|---:|---|---|
| 00 | Research map and learning contract | Complete |
| 01 | Repository and environment | Pending |
| 02 | Image arrays and tensors | Pending |
| 03 | Detection concepts | Pending |
| 04 | External-set protocol | Pending |
| 05 | TACO acquisition and integrity | Pending |
| 06 | Annotation audit | Pending |
| 07 | Coarse taxonomy | Pending |
| 08 | Annotation conversion | Pending |
| 09 | Data splits | Pending |
| 10 | E0 pretrained baseline | Pending |
| 11 | Tiny training experiment | Pending |
| 12 | E1 fine-tuned baseline | Pending |
| 13 | Internal evaluator | Pending |
| 14 | External and negative evaluation | Pending |
| 15 | Error analysis | Pending |
| 16 | E2 augmentation | Pending |
| 17 | E3 resolution | Pending |
| 18 | E4 taxonomy | Pending |
| 19 | Rebalancing decision | Pending |
| 20 | E5 confidence/review | Pending |
| 21 | Multi-seed confirmation | Pending |
| 22 | Efficiency benchmark | Pending |
| 23 | Image demo | Pending |
| 24 | Video and scientific handoff | Pending |

## 8. How to resume work

Use a message such as:

> Build Slice 00 from `ECOSORT_EDGE_BUILD_PLAN.md`. Do not start Slice 01.

For later slices, we will first confirm that the previous slice’s exit gate is satisfied. If the data or evidence contradicts a provisional choice, we will revise the affected **future** slices in this plan openly rather than quietly changing the project.

## 9. Scheduling note

The handbook lists **13 August 2026** as the completion target. This plan is ordered by learning and evidence, not compressed to force that date. Training and personal-image collection can consume wall-clock time, but parallel waiting does not authorize building later conceptual slices ahead of your understanding. If the date becomes a hard constraint, we should reduce experimental scope explicitly—not merge the explanation gates or pretend missing evidence exists.

## 10. Open decisions deliberately deferred

The following are real decisions, but choosing them now would give you conclusions without the evidence or concepts behind them:

- the exact Python and package versions, after Slice 01 inspects compatibility and hardware;
- the exact small YOLO variant, after the environment and baseline are understood;
- the final coarse-label mapping, after Slice 06 exposes the real category distribution;
- grouping versus stratified-approximation details, after the available TACO metadata is audited;
- whether class rebalancing is justified, after error evidence exists;
- whether an exported format adds a fair efficiency comparison, after the native benchmark works; and
- the simplest demo framework that supports the required review workflow, chosen in Slice 23.

These are not missing parts of the plan. Each is attached to the earliest slice where it can be decided transparently.

## 11. Source and scope note

This plan was derived only from the section titled **“Project 1 — EcoSort Edge”** in `AI_QML_Project_Handbook.docx`. The text beginning at **“Project 2 — CrisisSignal”** and all later projects were excluded.
