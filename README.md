# ASCII Art Generator

Convert images to ASCII art in the terminal using different character sets.

## Features
- Convert images to ASCII using:
  - Dense: `@%#*+=-:. `
  - Sparse: `#O+=- `
  - Binary: `10`
- Optional custom charset via `--chars`
- Optional color output using `termcolor`
- Width and charset CLI options
- Friendly validation errors for missing images and invalid options
- Pytest unit tests

## Install

```bash
pip install -r requirements.txt
```

## CLI Usage

```bash
python -m ascii_generator.cli image.jpg --width 120 --charset dense --color
```

Use a custom charset string:

```bash
python -m ascii_generator.cli image.jpg --width 120 --chars "@#:. "
```

If `--charset` is omitted, the default named set is `dense`.

## Run tests

```bash
PYTHONPATH=. pytest -q
```
