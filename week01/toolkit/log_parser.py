from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterator


@dataclass
class LogEvent:
    timestamp: datetime
    ip: str
    event: str
    user: str


def parse_line(line: str) -> LogEvent:
    """Parse one authentication log line."""
    parts = line.strip().split()

    if len(parts) != 4:
        raise ValueError(f"Malformed log line: {line!r}")

    timestamp_text, ip, event, user_text = parts

    try:
        timestamp = datetime.strptime(timestamp_text, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError as exc:
        raise ValueError(f"Invalid timestamp: {timestamp_text}") from exc

    if not user_text.startswith("user=") or not user_text[5:]:
        raise ValueError(f"Invalid user field: {user_text}")

    return LogEvent(timestamp, ip, event, user_text[5:])


def read_events(path: Path, bad_lines: list[str] | None = None) -> Iterator[LogEvent]:
    """Yield valid events, skipping malformed lines."""
    with path.open("r", encoding="utf-8") as file:
        for line in file:
            try:
                yield parse_line(line)
            except ValueError:
                if bad_lines is not None:
                    bad_lines.append(line.strip())
                continue
