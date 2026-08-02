# EcoSort Edge

EcoSort Edge is a reproducible litter-detection and environmental-auditing research project.

The project is being built as a reproducible empirical study of litter detection in real-world conditions. The foundation is now in place; no model, dataset, or training pipeline has been created yet.

Start here:

- [Project overview](PROJECT_OVERVIEW.md) — the public-facing project description, research questions, evaluation plan, and limitations.
- [Environment specification](environment.yml) — the clean-environment specification for reproducibility.

Run the environment smoke check with:

```bash
bash scripts/smoke_test.sh
```

The project will not claim municipal deployment, automatic recyclability decisions, autonomous robot control, or generalization beyond the evaluated data.

## Environment note

Local development uses the existing `pytorch-gpu` Conda environment. The repository’s `environment.yml` describes a clean environment for reproducing the project on another machine.
