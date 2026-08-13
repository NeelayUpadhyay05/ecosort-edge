"""Run the EcoSort Edge diagnostics and tests with the active Python."""

from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIRECTORY = REPOSITORY_ROOT / "src"


def project_environment() -> dict[str, str]:
    """Return an environment that can import the package from ``src``."""

    environment = os.environ.copy()
    existing_pythonpath = environment.get("PYTHONPATH")
    paths = [str(SOURCE_DIRECTORY)]
    if existing_pythonpath:
        paths.append(existing_pythonpath)
    environment["PYTHONPATH"] = os.pathsep.join(paths)
    return environment


def run_step(title: str, module: str) -> None:
    """Run one Python module and stop immediately if it fails."""

    print(f"== {title} ==", flush=True)
    subprocess.run(
        [sys.executable, "-m", module],
        cwd=REPOSITORY_ROOT,
        env=project_environment(),
        check=True,
    )


def main() -> None:
    run_step("EcoSort Edge environment diagnostics", "ecosort_edge")
    run_step("EcoSort Edge tests", "pytest")


if __name__ == "__main__":
    main()
