#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export PYTHONPATH="$repo_root/src${PYTHONPATH:+:$PYTHONPATH}"

echo "== EcoSort Edge environment diagnostics =="
conda run --no-capture-output -n pytorch-gpu python -m ecosort_edge

echo "== EcoSort Edge tests =="
conda run --no-capture-output -n pytorch-gpu python -m pytest
