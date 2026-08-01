# EcoSort Edge

EcoSort Edge is a lightweight litter-detection and environmental-auditing system for real-world images and video. It is designed to study not only whether a detector finds waste, but also how reliably it generalizes, how it behaves when uncertain, and what accuracy–efficiency trade-off is practical for edge-style hardware.

## Project status

The project is in development. Results will be added after the experiments are run; this document does not claim performance that has not yet been measured.

## Research questions

1. **Generalization:** How well does a lightweight detector fine-tuned on TACO perform on a small, independently collected litter test set?
2. **Taxonomy:** Does a smaller material-oriented label set improve reliable detection for rare classes compared with a fine-grained label set?
3. **Training interventions:** Which has the largest measured effect: transfer learning, augmentation, image resolution, or class rebalancing?
4. **Efficiency:** What accuracy–latency–model-size trade-off is available on GPU and CPU?
5. **Uncertainty and review:** Can a confidence-based review policy reduce harmful false positives without hiding too many useful detections?

These are empirical questions. Their hypotheses will be tested rather than presented as conclusions in advance.

## System boundary

### Inputs

- JPG or PNG images;
- webcam input; or
- recorded video.

### Outputs

- bounding boxes around detected litter;
- a documented coarse waste class;
- confidence for each detection;
- processing-speed information;
- low-confidence detections marked for human review; and
- an optional session summary.

### Out of scope

EcoSort Edge is not a municipal decision system, a recycling oracle, or an autonomous robot controller. Visual appearance cannot always determine material. Video counts may include the same object more than once without tracking, and results on TACO plus a small local test set cannot establish city-wide reliability.

## Data design

- **TACO:** The labeled source dataset, retained with annotation provenance and converted deterministically.
- **Coarse taxonomy:** A documented mapping from fine-grained source categories to a smaller set of learnable waste classes.
- **Independent external set:** Approximately 100–200 images collected before model tuning on that set, with privacy and safety precautions.
- **Negative set:** Clean streets, leaves, stones, signs, packaging-like textures, and indoor scenes without target litter to measure false alarms.

The external set remains untouched while the main modeling choices and confidence policy are selected.

## Modeling and comparisons

The project uses one small detector family to keep comparisons meaningful. The study includes:

- a generic pretrained detector baseline;
- a task-specific fine-tuned detector with coarse labels;
- controlled augmentation, resolution, taxonomy, and—when justified by the data—class-rebalancing comparisons;
- internal and frozen external evaluation; and
- a confidence threshold that determines when a detection should receive human review.

## Evaluation

Detection quality will be measured with mAP@0.5 and mAP@0.5:0.95, plus precision, recall, and per-class results when sample sizes support them. Analysis will also cover small, medium, and large objects; false positives per negative image; internal-versus-external performance; confidence behavior; and qualitative failure categories.

Efficiency reporting will include model file size, parameter count, median inference time, 95th-percentile inference time, and frames per second after warm-up on GPU and CPU.

## Demo behavior

The demo will accept unseen images and video, display detections and confidence, surface low-confidence items for review, and export a compact session result. It will make the counting limitation visible rather than implying that frame-wise detections automatically represent unique objects.

## Limitations

The system does not determine recyclability with certainty, does not replace human environmental auditing, and does not establish reliability outside the evaluated data. Small or biased external samples may support aggregate conclusions but not precise per-class claims. Any future tracking, broader collection, or operational deployment would require separate validation.

## Reproducibility

The implementation will keep data mappings, split rules, training settings, evaluation settings, inference settings, package versions, seeds, checkpoints, and result tables associated with each experiment. Reproduction commands and the final model card will be added as the implementation develops.
