import sys
from pathlib import Path

sys.path.insert(0, "week01")

from toolkit.log_parser import parse_line

log_path = Path("week01/data/auth_practice.log")

valid = 0
invalid = []

with log_path.open("r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        try:
            parse_line(line)
            valid += 1
        except ValueError:
            invalid.append((line_number, line.strip()))

print("Valid lines:", valid)
print("Invalid lines:", len(invalid))

for line_number, line in invalid:
    print(line_number, line)