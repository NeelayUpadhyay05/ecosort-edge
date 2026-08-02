"""Small, explicit image-to-tensor transformations for learning."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import torch
from PIL import Image


def load_rgb_image(path: str | Path) -> Image.Image:
    """Load an image and make its channel order explicitly RGB."""

    with Image.open(path) as image:
        return image.convert("RGB")


def image_to_chw_tensor(image: Image.Image) -> torch.Tensor:
    """Convert an RGB PIL image from HWC uint8 pixels to CHW uint8 tensor."""

    width, height = image.size
    # Pillow 14 deprecates ``getdata`` in favor of ``get_flattened_data``.
    # Keep the fallback so this teaching utility also works with older Pillow.
    if hasattr(image, "get_flattened_data"):
        pixels = list(image.get_flattened_data())
    else:
        pixels = list(image.getdata())
    height_width_channels = torch.tensor(pixels, dtype=torch.uint8).reshape(
        height, width, 3
    )
    return height_width_channels.permute(2, 0, 1).contiguous()


def resize_rgb_image(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    """Resize an RGB image using Pillow's bilinear resampling."""

    return image.resize(size, Image.Resampling.BILINEAR)


def normalize_to_unit_range(tensor: torch.Tensor) -> torch.Tensor:
    """Convert uint8 pixels in [0, 255] to float pixels in [0, 1]."""

    return tensor.to(dtype=torch.float32) / 255.0


def describe_tensor(tensor: torch.Tensor) -> dict[str, Any]:
    """Return the facts a learner should inspect after a transformation."""

    return {
        "shape": list(tensor.shape),
        "dtype": str(tensor.dtype),
        "min": float(tensor.min().item()),
        "max": float(tensor.max().item()),
    }


def build_learning_report(
    input_path: str | Path,
    output_dir: str | Path,
    resized_size: tuple[int, int] = (8, 8),
) -> dict[str, Any]:
    """Create a side-by-side image and JSON facts for one transformation run."""

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    original = load_rgb_image(input_path)
    resized = resize_rgb_image(original, resized_size)
    original_tensor = image_to_chw_tensor(original)
    resized_tensor = image_to_chw_tensor(resized)
    normalized_tensor = normalize_to_unit_range(resized_tensor)

    comparison = Image.new("RGB", (original.width + resized.width, max(original.height, resized.height)), "white")
    comparison.paste(original, (0, 0))
    comparison.paste(resized, (original.width, 0))
    comparison.save(output_path / "comparison.png")

    report = {
        "input": str(input_path),
        "channel_order": "RGB",
        "original_tensor": describe_tensor(original_tensor),
        "resized_tensor": describe_tensor(resized_tensor),
        "normalized_resized_tensor": describe_tensor(normalized_tensor),
    }
    (output_path / "stats.json").write_text(json.dumps(report, indent=2) + "\n")
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Path to an image file")
    parser.add_argument("--output", default="outputs/image_lab", help="Output directory")
    args = parser.parse_args()

    report = build_learning_report(args.input, args.output)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
