from pathlib import Path
from toolkit.loader import DataLoader
from toolkit.log_parser import read_events


def main():
    base_dir = Path(__file__).parent
    loader = DataLoader(base_dir / "data")

    events = list(read_events(base_dir / "data" / "auth.log"))

    print(f"Total valid events: {len(events)}")
    print(f"CSV records: {len(loader.load_csv('sample.csv'))}")


if __name__ == "__main__":
    main()
