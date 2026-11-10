import pytest
from pathlib import Path

from week01.toolkit.log_parser import parse_line, read_events


def test_parse_valid_line():
    event = parse_line("2026-11-09T10:30:00Z 192.168.1.5 LOGIN_SUCCESS user=ali")
    assert event.ip == "192.168.1.5"
    assert event.event == "LOGIN_SUCCESS"
    assert event.user == "ali"


def test_parse_invalid_line():
    with pytest.raises(ValueError):
        parse_line("invalid line")


def test_parse_invalid_timestamp():
    with pytest.raises(ValueError):
        parse_line("wrong-time 192.168.1.5 LOGIN_SUCCESS user=ali")

def test_read_events_skips_corrupted_lines(tmp_path):
    log_file = tmp_path / "test.log"
    log_file.write_text(
        "2026-11-09T10:30:00Z 192.168.1.5 LOGIN_SUCCESS user=ali\n"
        "invalid line\n"
        "2026-11-09T10:35:00Z 192.168.1.6 LOGIN_FAILED user=ahmed\n",
        encoding="utf-8",
    )

    events = list(read_events(log_file))

    assert len(events) == 2
    assert events[0].user == "ali"
    assert events[1].user == "ahmed"
