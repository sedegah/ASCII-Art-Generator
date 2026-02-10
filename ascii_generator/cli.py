from __future__ import annotations

import argparse
from pathlib import Path

from termcolor import colored

from ascii_generator.convert import CHARSETS, image_to_ascii


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert image to ASCII art.")
    parser.add_argument("image", help="Path to input image")
    parser.add_argument("--width", type=int, default=100, help="Output ASCII width")
    parser.add_argument(
        "--charset",
        default="dense",
        choices=sorted(CHARSETS.keys()),
        help="Charset type",
    )
    parser.add_argument("--color", action="store_true", help="Enable colored ASCII output")

    args = parser.parse_args()

    image_path = Path(args.image)
    if not image_path.exists() or not image_path.is_file():
        parser.error(f"Input image does not exist: {args.image}")
    if args.width <= 0:
        parser.error("--width must be a positive integer")

    ascii_art = image_to_ascii(image_path, width=args.width, charset_name=args.charset)

    if args.color:
        for line in ascii_art.splitlines():
            print(colored(line, "cyan"))
    else:
        print(ascii_art)


if __name__ == "__main__":
    main()
