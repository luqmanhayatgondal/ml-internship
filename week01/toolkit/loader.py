import csv
import json
from pathlib import Path


class DataLoader:
    """Load CSV, JSON and text files."""

    def __init__(self, base_dir: Path):
        self.base_dir = base_dir

    def _get_path(self, name: str) -> Path:
        """Return file path or raise an error if missing."""
        path = self.base_dir / name

        if not path.exists():
            raise FileNotFoundError(f"File not found: {path}")

        return path

    def load_csv(self, name: str) -> list[dict]:
        """Load CSV data as a list of dictionaries."""
        path = self._get_path(name)

        with path.open("r", encoding="utf-8", newline="") as file:
            return list(csv.DictReader(file))

    def load_json(self, name: str):
        """Load and return JSON data."""
        path = self._get_path(name)

        with path.open("r", encoding="utf-8") as file:
            return json.load(file)

    def load_lines(self, name: str) -> list[str]:
        """Load a text file and return its lines."""
        path = self._get_path(name)

        with path.open("r", encoding="utf-8") as file:
            return file.readlines()
