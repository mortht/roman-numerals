import pytest
from roman_cli.converter import int_to_roman, roman_to_int, RomanError


@pytest.mark.parametrize("s,n", [("MCMXCIV", 1994), ("IV", 4), ("MMMCMXCIX", 3999),
                                 ("I", 1), ("mcmxciv", 1994), ("McmXciv", 1994)])
def test_valid(s, n):
    assert roman_to_int(s) == n


def test_invalid_chars_named():
    with pytest.raises(RomanError) as e:
        roman_to_int("ABC")
    assert "A" in str(e.value) and "B" in str(e.value)


@pytest.mark.parametrize("s", ["", "IIII", "VX", "IC", "IIX", "VV", "MMMM",
                               "IL", "XM", "VIV", "IXI", "iiii", "XXXX", "DD", "LL", "IVI"])
def test_rejected(s):
    with pytest.raises(RomanError):
        roman_to_int(s)


@pytest.mark.parametrize("s", ["X1", "I V", "Ⅳ", "MCMXCIV!"])
def test_bad_chars(s):
    with pytest.raises(RomanError):
        roman_to_int(s)


def test_round_trip():
    for n in range(1, 4000):
        assert roman_to_int(int_to_roman(n)) == n
