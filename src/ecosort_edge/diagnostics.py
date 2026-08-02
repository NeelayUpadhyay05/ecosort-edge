"""Report the software and hardware context used by the project."""

from __future__ import annotations

import importlib
import platform
import sys
from typing import Any


def _module_version(module_name: str) -> str:
    """Return a module version, or a clear message when it is unavailable."""

    try:
        module = importlib.import_module(module_name)
    except ImportError:
        return "not installed"
    return str(getattr(module, "__version__", "installed"))


def collect_diagnostics() -> dict[str, Any]:
    """Collect facts that make a run's environment understandable."""

    details: dict[str, Any] = {
        "python_version": platform.python_version(),
        "python_executable": sys.executable,
        "platform": platform.platform(),
        "torch_version": _module_version("torch"),
        "cuda_available": False,
        "cuda_version": "unavailable",
        "gpu_name": "unavailable",
    }

    try:
        torch = importlib.import_module("torch")
    except ImportError:
        return details

    details["cuda_available"] = bool(torch.cuda.is_available())
    details["cuda_version"] = str(torch.version.cuda or "not reported")
    if details["cuda_available"]:
        details["gpu_name"] = str(torch.cuda.get_device_name(0))
    return details


def main() -> None:
    """Print diagnostics in a stable, readable order."""

    for key, value in collect_diagnostics().items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
