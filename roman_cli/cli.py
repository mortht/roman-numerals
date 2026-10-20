"""Thin CLI layer."""

import sys

from roman_cli.converter import RomanError, int_to_roman, roman_to_int

USAGE = "usage: python -m roman_cli <value>"


def _is_ascii_digits(s: str) -> bool:
    return s.isascii() and s.isdigit()


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if len(args) != 1:
        print(USAGE, file=sys.stderr)
        return 2
    value = args[0]
    try:
        body = value[1:] if value.startswith("-") else value
        if body and _is_ascii_digits(body):
            if len(body) > 10:  # avoid int() digit limit; surely out of range
                raise RomanError("number out of range; valid range is 1-3999")
            result = int_to_roman(int(value))
        elif value.isascii() and value.isalpha():
            result = str(roman_to_int(value))
        else:
            raise RomanError(f"invalid input: {value!r}")
    except RomanError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    print(result)
    return 0
