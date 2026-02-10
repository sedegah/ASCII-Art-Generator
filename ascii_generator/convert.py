from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image

CHARSETS = {
    "dense": "@%#*+=-:. ",
    "sparse": "#O+=- ",
    "binary": "10",
}


def get_ascii_char(pixel_value: int, charset: str) -> str:
    """Map a grayscale pixel value (0-255) to a character in the provided charset."""
    if not charset:
        raise ValueError("Charset must contain at least one character.")

    clamped = max(0, min(255, int(pixel_value)))
    index = int(clamped / 255 * (len(charset) - 1))
    return charset[index]


def image_to_ascii(path: str | Path, width: int = 100, charset_name: str = "dense") -> str:
    """Convert an image to ASCII art text."""
    if width <= 0:
        raise ValueError("Width must be a positive integer.")

    charset = CHARSETS.get(charset_name, CHARSETS["dense"])

    img = Image.open(path).convert("L")
    w, h = img.size
    aspect_ratio = h / w
    height = max(1, int(aspect_ratio * width * 0.55))
    img = img.resize((width, height))

    pixels = np.array(img)
    ascii_img = np.vectorize(lambda px: get_ascii_char(px, charset))(pixels)
    lines = ["".join(row) for row in ascii_img]
    return "\n".join(lines)
