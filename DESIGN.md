# Design: roman-cli

_The approved design of run 14d32e0e (2026-10-20), kept up to date by agent-platform. Edit it freely and commit the edit: the next run reads it as it is._

## Architecture

Small package: pure conversion module separate from thin CLI layer

## Tech stack

- Stack: `python` (Python 3.14 with pytest)
- Python 3.14
- standard library only
- pytest

## Dependencies

None beyond the Python standard library and pytest.

## Components

### converter

Pure integer<->Roman conversion and validation; raises RomanError

- Interface: `class RomanError(ValueError); int_to_roman(n: int) -> str; roman_to_int(s: str) -> int`

### cli

Parse argv, auto-detect direction, print result to stdout or one-line error to stderr, return exit code

- Interface: `main(argv: list[str] | None = None) -> int; python -m roman_cli <value>`
- Uses: converter

## Shared conventions

Package name: roman_cli (roman_cli/__init__.py, converter.py, cli.py, __main__.py); tests in tests/ (test_converter.py, test_cli.py). Tests import `from roman_cli.converter import ...`; add a tests-friendly layout (run pytest from project root; include empty conftest.py at root if needed so the package imports). Exit codes: 0 success, 2 any invalid input or usage error. Errors: 'error: <message>' single line on stderr. Canonical Roman numerals only, uppercase output.

## Risks

- Negative numbers like '-5' may be mistaken for options by argparse; handle argv manually
- Non-canonical detection must be exact (use strict regex ^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$)
