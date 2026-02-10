from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image

CHARSETS = {
    "dense": "@%#*+=-:. ",
    "sparse": "#O+=- ",
    "binary": "10",
}
DEFAULT_CHARSET = "dense"
CHAR_HEIGHT_RATIO = 0.55


def _resolve_charset(charset_name: str = DEFAULT_CHARSET, charset: str | None = None) -> str:
    """Resolve the effective charset from a name or explicit value."""
    if charset is not None:
        if not charset:
            raise ValueError("Charset must contain at least one character.")
        return charset

    if charset_name not in CHARSETS:
        valid = ", ".join(sorted(CHARSETS.keys()))
        raise ValueError(f"Unknown charset '{charset_name}'. Valid choices: {valid}")

    return CHARSETS[charset_name]


def get_ascii_char(pixel_value: int, charset: str) -> str:
    """Map a grayscale pixel value (0-255) to a character in the provided charset."""
    if not charset:
        raise ValueError("Charset must contain at least one character.")

    clamped = max(0, min(255, int(pixel_value)))
    index = int(clamped / 255 * (len(charset) - 1))
    return charset[index]


def image_to_ascii(
    path: str | Path,
    width: int = 100,
    charset_name: str = DEFAULT_CHARSET,
    charset: str | None = None,
) -> str:
    """Convert an image to ASCII art text."""
    if width <= 0:
        raise ValueError("Width must be a positive integer.")

    image_path = Path(path)
    if not image_path.exists() or not image_path.is_file():
        raise ValueError(f"Input image does not exist: {path}")

    resolved_charset = _resolve_charset(charset_name, charset)

    try:
        with Image.open(image_path) as source:
            img = source.convert("L")
    except OSError as exc:
        raise ValueError(f"Failed to read image '{path}': {exc}") from exc

    w, h = img.size
    if w <= 0 or h <= 0:
        raise ValueError("Image dimensions must be positive.")

    aspect_ratio = h / w
    height = max(1, int(aspect_ratio * width * CHAR_HEIGHT_RATIO))
    img = img.resize((width, height), resample=Image.Resampling.BICUBIC)

    pixels = np.array(img, dtype=np.uint8)
    indices = (pixels.astype(np.float32) / 255 * (len(resolved_charset) - 1)).astype(np.int32)
    lookup = np.array(list(resolved_charset))
    ascii_img = lookup[indices]

    return "\n".join("".join(row) for row in ascii_img)
