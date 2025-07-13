# ASCII Art Generator

Convert images to ASCII art in the terminal using different character sets.

## Features
- Convert images to ASCII using:
  - Dense: `@%#*+=-:. `
  - Sparse: `#O+=- `
  - Binary: `10`
- Optional color output using `termcolor`
- CLI with flexible options
- Pytest unit tests
- GitHub Actions CI

## CLI Usage

```bash
python -m ascii_generator.cli image.jpg --width 120 --charset dense --color
