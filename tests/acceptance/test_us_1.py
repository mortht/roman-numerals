import pytest
from roman_cli.converter import int_to_roman, RomanError


@pytest.mark.parametrize("n,r", [(1, "I"), (4, "IV"), (9, "IX"), (14, "XIV"),
                                 (1994, "MCMXCIV"), (3999, "MMMCMXCIX"),
                                 (2000, "MM"), (400, "CD"), (3888, "MMMDCCCLXXXVIII")])
def test_values(n, r):
    assert int_to_roman(n) == r


@pytest.mark.parametrize("n", [0, -5, -1, 4000, 4001, 10**9])
def test_out_of_range(n):
    with pytest.raises(RomanError, match="1-3999"):
        int_to_roman(n)


def test_error_is_valueerror():
    assert issubclass(RomanError, ValueError)
