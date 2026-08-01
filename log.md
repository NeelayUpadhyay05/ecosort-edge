# EcoSort Edge — Change Log

This file is updated whenever project code is created or changed. During the planning and setup slices, documentation and repository changes are recorded too so the project history stays understandable.

## Entry format

For each change, record:

- date;
- slice;
- files created or changed;
- what changed and why;
- verification performed; and
- environment note, including whether Conda was created or changed.

## 2026-08-01 — Slice 00

### Created

- `PROJECT_CHARTER.md` — the research questions, hypotheses, system boundary, non-claims, and E0–E5 experiment map.
- `ECOSORT_EDGE_BUILD_PLAN.md` — marked Slice 00 complete in the canonical progress tracker.
- `artifact.json` and `ECOSORT_EDGE_BUILD_PLAN.html` — refreshed the generated reading copy to match the completed tracker.
- `README.md` — minimal GitHub-facing project entry point.
- `.gitignore` — excludes local environments, datasets, model weights, run outputs, and tooling caches.
- `log.md` — this change log and future entry template.

### Repository action

- Initialized a local Git repository on the `main` branch.
- Created initial commit `e9c10a4` (`Complete Slice 00 project charter`).

### Verification

- Confirmed the charter matches Slice 00 of `ECOSORT_EDGE_BUILD_PLAN.md`.
- Confirmed no Python, model, dataset, training, or demo code was created.
- Confirmed the five research questions, explicit non-claims, and E0–E5 map are present.

### Environment note

- No Conda environment or environment file was created. Before Slice 01 creates one, the project owner must provide the requested environment details.

## 2026-08-01 — Repository artifact audit

### Decision

- Keep tracked: the Markdown plan, project charter, README, change log, `.gitignore`, generated portable plan HTML, and its `artifact.json` source payload.
- Keep the generated plan artifacts because they are small, contain no credentials or machine-local paths, and provide a reproducible/shareable reading copy of the canonical plan.
- Ignore future raw/processed/external/negative datasets, model checkpoints and exports, training/evaluation outputs, local environments, caches, editor files, and credential files.

### Verification

- Audited every file currently in the folder; no Python source, dataset, model weight, environment file, or secret was present.
- Confirmed the generated HTML and JSON contain only the plan/report content and safe source metadata.
- Confirmed `origin/main` already matched the local repository before this cleanup.

### Environment note

- No Conda environment was created or changed.

## Future entry template

## YYYY-MM-DD — Slice NN

### Changed

- Files:
- Purpose:

### Verification

- Commands/checks:
- Result:

### Environment note

- Conda/environment action:
