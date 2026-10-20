import pytest

from roman_cli.converter import RomanError, int_to_roman, roman_to_int


@pytest.mark.parametrize("n,r", [(1, "I"), (4, "IV"), (9, "IX"), (14, "XIV"),
                                 (1994, "MCMXCIV"), (3999, "MMMCMXCIX")])
def test_int_to_roman(n, r):
    assert int_to_roman(n) == r
    assert roman_to_int(r) == n


@pytest.mark.parametrize("n", [0, -5, 4000])
def test_int_out_of_range(n):
    with pytest.raises(RomanError, match="1-3999"):
        int_to_roman(n)


def test_lowercase():
    assert roman_to_int("mcmxciv") == 1994


def test_invalid_chars():
    with pytest.raises(RomanError, match="invalid characters: AB"):
        roman_to_int("ABC")


@pytest.mark.parametrize("s", ["", "IIII", "VX", "IC", "IIX", "VV", "MMMM"])
def test_invalid(s):
    with pytest.raises(RomanError):
        roman_to_int(s)


def test_round_trip():
    for n in range(1, 4000):
        assert roman_to_int(int_to_roman(n)) == n
