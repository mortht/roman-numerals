# roman_cli

A small command-line tool that converts between integers and Roman numerals.
The argument type is detected automatically.

## Features

- Integer to Roman numeral (1–3999), uppercase output.
- Roman numeral to integer; input is case-insensitive. On the command line, whitespace around the value is rejected as invalid input (only `roman_to_int` called from Python strips surrounding whitespace).
- Input detection in the CLI: an ASCII integer (an optional leading `-` is allowed) is converted to Roman; an ASCII alphabetic string is converted to an integer; anything else gives `error: invalid input: '<value>'`. Integers with more than 10 digits give `error: number out of range; valid range is 1-3999`.
- Only canonical numerals are accepted (e.g. `IIII` and `IC` are rejected).
- Errors are printed as a single line `error: <message>` on stderr; exit code 2 for any invalid input or usage error, 0 on success.

## Requirements and install

- Python 3.14 or newer (`requires-python = ">=3.14"`).
- No runtime dependencies (standard library only); pytest is needed for the tests.
- No build step: run from the project root with `python -m roman_cli`. The project is not set up for `pip install` (no build system configured) and installs no console script.

## Usage

```
python -m roman_cli <value>
```

```
$ python -m roman_cli 1994
MCMXCIV
$ python -m roman_cli mcmxciv
1994
$ python -m roman_cli 4000
error: 4000 is out of range; valid range 1-3999
$ python -m roman_cli IIII
error: non-canonical Roman numeral: IIII
```

Exactly one argument is required; otherwise `usage: python -m roman_cli <value>` goes to stderr and the exit code is 2.

The converter can also be used from Python:

```python
from roman_cli.converter import int_to_roman, roman_to_int, RomanError
int_to_roman(14)     # "XIV"
roman_to_int("XIV")  # 14
```

## Running the tests

```
python -m pytest
```

## Project structure

- `roman_cli/converter.py` – pure conversion logic: `int_to_roman`, `roman_to_int`, and `RomanError` (a `ValueError`).
- `roman_cli/cli.py` – thin CLI layer: `main(argv)` detects input type, prints results or errors, returns the exit code.
- `roman_cli/__main__.py` – entry point for `python -m roman_cli`.
- `tests/` – pytest tests (`test_converter.py`, `test_cli.py`) and `tests/acceptance/`.
- `conftest.py`, `pyproject.toml` – project and pytest configuration.
- `DESIGN.md`, `SPECIFICATION.md` – design and specification documents.
