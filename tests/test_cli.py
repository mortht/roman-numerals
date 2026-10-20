import subprocess
import sys

import pytest

from roman_cli.cli import main


def test_int_to_roman(capsys):
    assert main(["1994"]) == 0
    assert capsys.readouterr().out == "MCMXCIV\n"


def test_roman_to_int(capsys):
    assert main(["mcmxciv"]) == 0
    assert capsys.readouterr().out == "1994\n"


@pytest.mark.parametrize("v", ["0", "-5", "4000"])
def test_range(v, capsys):
    assert main([v]) == 2
    c = capsys.readouterr()
    assert c.out == "" and "1-3999" in c.err


@pytest.mark.parametrize("v", ["abc3", "3.5", "", "ABC", "IIII", "VX"])
def test_invalid(v, capsys):
    assert main([v]) == 2
    c = capsys.readouterr()
    assert c.out == "" and c.err.startswith("error: ")
    assert len(c.err.strip().splitlines()) == 1


@pytest.mark.parametrize("a", [[], ["1", "2"]])
def test_usage(a, capsys):
    assert main(a) == 2
    c = capsys.readouterr()
    assert c.out == "" and "usage" in c.err


def test_subprocess():
    r = subprocess.run([sys.executable, "-m", "roman_cli", "-5"],
                       capture_output=True, text=True)
    assert r.returncode == 2 and r.stdout == ""
    assert "Traceback" not in r.stderr and "1-3999" in r.stderr
    r = subprocess.run([sys.executable, "-m", "roman_cli", "1994"],
                       capture_output=True, text=True)
    assert r.returncode == 0 and r.stdout == "MCMXCIV\n"
