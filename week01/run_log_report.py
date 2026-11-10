import sys
from pathlib import Path
from toolkit.loader import DataLoader
from toolkit.log_parser import read_events


def main():
    base_dir = Path(__file__).parent
    loader = DataLoader(base_dir / "data")

    if len(sys.argv) > 1:
        log_path = Path(sys.argv[1])
    else:
        log_path = base_dir / "data" / "auth.log"

    bad_lines = []
    events = list(read_events(log_path, bad_lines))

    print(f"Total lines: {len(events) + len(bad_lines)}")
    print(f"Total valid events: {len(events)}")
    print(f"Corrupted lines: {len(bad_lines)}")
    print(f"CSV records: {len(loader.load_csv('sample.csv'))}")


if __name__ == "__main__":
    main()
