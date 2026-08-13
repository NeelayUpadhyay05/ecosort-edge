# EcoSort Edge

EcoSort Edge is a reproducible litter-detection and environmental-auditing research project.

The project is being built as a reproducible empirical study of litter detection in real-world conditions. The foundation is now in place; no model, dataset, or training pipeline has been created yet.

Start here:

- [Project overview](PROJECT_OVERVIEW.md) — the public-facing project description, research questions, evaluation plan, and limitations.
- [Environment specification](environment.yml) — the clean-environment specification for reproducibility.

Activate a Conda environment containing the dependencies, then run the
cross-platform environment smoke check from the repository root:

```text
python scripts/smoke_test.py
```

The project will not claim municipal deployment, automatic recyclability decisions, autonomous robot control, or generalization beyond the evaluated data.

## Environment note

The repository’s `environment.yml` describes a clean environment for reproducing
the project. Install the PyTorch build appropriate for the operating system and,
when applicable, the machine's CUDA support.
