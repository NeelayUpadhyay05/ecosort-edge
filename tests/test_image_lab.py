from PIL import Image
import torch

from ecosort_edge.image_lab import (
    image_to_chw_tensor,
    normalize_to_unit_range,
    resize_rgb_image,
)


def test_rgb_image_becomes_channel_first_tensor() -> None:
    image = Image.new("RGB", (2, 3), (255, 0, 128))

    tensor = image_to_chw_tensor(image)

    assert tensor.shape == (3, 3, 2)
    assert tensor.dtype == torch.uint8
    assert tensor[:, 0, 0].tolist() == [255, 0, 128]


def test_resize_and_normalize_have_expected_ranges() -> None:
    image = Image.new("RGB", (2, 3), (255, 128, 0))

    resized = resize_rgb_image(image, (4, 5))
    normalized = normalize_to_unit_range(image_to_chw_tensor(resized))

    assert resized.size == (4, 5)
    assert normalized.shape == (3, 5, 4)
    assert normalized.dtype == torch.float32
    assert 0.0 <= normalized.min() <= normalized.max() <= 1.0
