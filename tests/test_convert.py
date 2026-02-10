from pathlib import Path

import pytest
from PIL import Image

from ascii_generator.convert import CHARSETS, get_ascii_char, image_to_ascii


def test_ascii_mapping_bounds():
    dense = CHARSETS["dense"]
    assert get_ascii_char(0, dense) == dense[0]
    assert get_ascii_char(255, dense) == dense[-1]


def test_ascii_mapping_clamps_values():
    sparse = CHARSETS["sparse"]
    assert get_ascii_char(-10, sparse) == sparse[0]
    assert get_ascii_char(999, sparse) == sparse[-1]


def test_empty_charset_raises_value_error():
    with pytest.raises(ValueError, match="Charset"):
        get_ascii_char(128, "")


def test_charset_selection_is_valid():
    for key, value in CHARSETS.items():
        assert isinstance(key, str)
        assert isinstance(value, str)
        assert len(value) > 0


def test_image_to_ascii_generates_output(tmp_path: Path):
    image_path = tmp_path / "tiny.png"
    image = Image.new("L", (10, 10), color=0)
    image.save(image_path)

    output = image_to_ascii(image_path, width=10, charset_name="binary")
    lines = output.splitlines()

    assert len(lines) > 0
    assert all(len(line) == 10 for line in lines)
    assert set("".join(lines)).issubset(set(CHARSETS["binary"]))


def test_image_to_ascii_rejects_non_positive_width(tmp_path: Path):
    image_path = tmp_path / "tiny.png"
    Image.new("L", (2, 2), color=120).save(image_path)

    with pytest.raises(ValueError, match="Width"):
        image_to_ascii(image_path, width=0)


def test_image_to_ascii_rejects_unknown_charset(tmp_path: Path):
    image_path = tmp_path / "tiny.png"
    Image.new("L", (2, 2), color=120).save(image_path)

    with pytest.raises(ValueError, match="Unknown charset"):
        image_to_ascii(image_path, width=10, charset_name="unknown")


def test_image_to_ascii_accepts_custom_charset(tmp_path: Path):
    image_path = tmp_path / "tiny.png"
    Image.new("L", (3, 3), color=255).save(image_path)

    output = image_to_ascii(image_path, width=3, charset=".X")
    assert set(output.replace("\n", "")) == {"X"}
