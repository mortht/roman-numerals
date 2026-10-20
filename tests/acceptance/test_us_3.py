import subprocess
import sys
import pytest


def run(*args):
    return subprocess.run([sys.executable, "-m", "roman_cli", *args],
                          capture_output=True, text=True)


@pytest.mark.parametrize("arg", ["0", "-5", "4000", "abc3", "3.5", "", "ABC",
                                 "IIII", "VX", "-0", " 5", "5 ", "12a", "Ⅳ"])
def test_errors(arg):
    r = run(arg)
    assert r.returncode == 2
    assert r.stdout == ""
    assert "Traceback" not in r.stderr
    assert r.stderr.startswith("error:")
    assert len(r.stderr.strip().splitlines()) == 1


@pytest.mark.parametrize("args", [[], ["1", "2"], ["I", "II", "III"]])
def test_usage(args):
    r = run(*args)
    assert r.returncode == 2
    assert r.stdout == ""
    assert r.stderr.strip()
    assert "Traceback" not in r.stderr


def test_direction_detection():
    assert run("14").stdout == "XIV\n"
    assert run("xiv").stdout == "14\n"


def test_main_inprocess(capsys):
    from roman_cli.cli import main
    assert main(["-5"]) == 2
    c = capsys.readouterr()
    assert c.out == "" and "1-3999" in c.err
    assert main([]) == 2
    c = capsys.readouterr()
    assert c.out == "" and c.err
    assert main(["1994"]) == 0
    assert capsys.readouterr().out == "MCMXCIV\n"
