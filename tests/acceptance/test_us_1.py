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


def _run(*args):
    import subprocess, sys
    return subprocess.run([sys.executable, "-m", "roman_cli", *args],
                          capture_output=True, text=True)


@pytest.mark.parametrize("n,r", [("1", "I"), ("4", "IV"), ("9", "IX"), ("14", "XIV"),
                                 ("1994", "MCMXCIV"), ("3999", "MMMCMXCIX")])
def test_cli_ok(n, r):
    p = _run(n)
    assert p.returncode == 0 and p.stdout == r + "\n" and p.stderr == ""


@pytest.mark.parametrize("n", ["0", "-5", "4000", "99999"])
def test_cli_range(n):
    p = _run(n)
    assert p.returncode == 2 and p.stdout == "" and "1-3999" in p.stderr


@pytest.mark.parametrize("n", ["abc3", "3.5", ""])
def test_cli_non_integer(n):
    p = _run(n)
    assert p.returncode == 2 and p.stdout == "" and p.stderr.startswith("error:")


def test_error_is_valueerror():
    assert issubclass(RomanError, ValueError)
