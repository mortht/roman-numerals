from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def _text():
    return (ROOT / "README.md").read_text(encoding="utf-8")


def test_exists():
    assert (ROOT / "README.md").is_file()
    assert len(_text().strip()) > 200


def test_purpose():
    t = _text().lower()
    assert "roman" in t and "integer" in t and "feature" in t


def test_install_and_run():
    t = _text()
    assert "3.14" in t
    assert "python -m roman_cli" in t
    assert "depend" in t.lower()
    assert "pyproject.toml" in t


def test_tests_command():
    assert "python -m pytest" in _text() or "pytest" in _text()


def test_structure():
    t = _text()
    for m in ("converter.py", "cli.py", "__main__.py", "tests"):
        assert m in t
    for name in ("int_to_roman", "roman_to_int", "RomanError", "main"):
        assert name in t
