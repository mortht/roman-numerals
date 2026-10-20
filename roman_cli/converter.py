"""Pure integer <-> Roman numeral conversion."""

import re

_PAIRS = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
]
_VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
_CANONICAL = re.compile(
    r"M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})"
)


class RomanError(ValueError):
    """Invalid input for Roman numeral conversion."""


def int_to_roman(n: int) -> str:
    if isinstance(n, bool) or not isinstance(n, int):
        raise RomanError(f"not an integer: {n!r}; valid range 1-3999")
    if not 1 <= n <= 3999:
        raise RomanError(f"{n} is out of range; valid range 1-3999")
    out = []
    for value, sym in _PAIRS:
        while n >= value:
            out.append(sym)
            n -= value
    return "".join(out)


def roman_to_int(s: str) -> int:
    if not isinstance(s, str):
        raise RomanError(f"not a string: {s!r}")
    s = s.strip().upper()
    if not s:
        raise RomanError("empty input")
    bad = sorted({c for c in s if c not in _VALUES})
    if bad:
        raise RomanError(f"invalid characters: {''.join(bad)}")
    if not _CANONICAL.fullmatch(s):
        raise RomanError(f"non-canonical Roman numeral: {s}")
    total = 0
    for i, c in enumerate(s):
        v = _VALUES[c]
        if i + 1 < len(s) and _VALUES[s[i + 1]] > v:
            total -= v
        else:
            total += v
    return total
