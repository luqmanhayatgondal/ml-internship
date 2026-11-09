import json

import pytest

from week01.toolkit.loader import DataLoader


def test_load_csv(tmp_path):
    file = tmp_path / "sample.csv"
    file.write_text("name,age\nAli,20\nSara,22\n", encoding="utf-8")

    loader = DataLoader(tmp_path)
    result = loader.load_csv("sample.csv")

    assert len(result) == 2
    assert result[0]["name"] == "Ali"


def test_load_json(tmp_path):
    file = tmp_path / "sample.json"
    file.write_text(json.dumps({"name": "Ali"}), encoding="utf-8")

    loader = DataLoader(tmp_path)

    assert loader.load_json("sample.json") == {"name": "Ali"}


def test_load_lines(tmp_path):
    file = tmp_path / "sample.txt"
    file.write_text("Hello\nWorld\n", encoding="utf-8")

    loader = DataLoader(tmp_path)

    assert loader.load_lines("sample.txt") == ["Hello\n", "World\n"]


def test_missing_file():
    loader = DataLoader(__import__("pathlib").Path("missing_folder"))

    with pytest.raises(FileNotFoundError):
        loader.load_csv("missing.csv")
