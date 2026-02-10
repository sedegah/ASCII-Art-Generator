# ASCII Art Generator

Convert images to ASCII art in the terminal using different character sets.

## Features
- Convert images to ASCII using:
  - Dense: `@%#*+=-:. `
  - Sparse: `#O+=- `
  - Binary: `10`
- Optional color output using `termcolor`
- Width and charset CLI options
- Pytest unit tests

## Install

```bash
pip install -r requirements.txt
```

## CLI Usage

```bash
python -m ascii_generator.cli image.jpg --width 120 --charset dense --color
```

## Run tests

```bash
PYTHONPATH=. pytest -q
```
