
from pathlib import Path
from collections import Counter, defaultdict


def parse_line(line):
    parts = line.strip().split()

    if len(parts) != 4:
        raise ValueError("Invalid log line")

    timestamp, ip, event, user_text = parts

    if not timestamp.endswith("Z") or not user_text.startswith("user="):
        raise ValueError("Invalid log format")

    return {
        "timestamp": timestamp,
        "ip": ip,
        "event": event,
        "user": user_text[5:]
    }


def read_events(path):
    valid_events = []
    corrupted_lines = []

    with path.open("r", encoding="utf-8") as file:
        for line in file:
            try:
                event = parse_line(line)
                valid_events.append(event)
            except ValueError:
                corrupted_lines.append(line.strip())

    return valid_events, corrupted_lines


def analyze_events(events):
    ip_counts = Counter()
    event_counts = Counter()
    failed_logins = defaultdict(Counter)

    for event in events:
        ip_counts[event["ip"]] += 1
        event_counts[event["event"]] += 1

        if event["event"] == "LOGIN_FAILED":
            failed_logins[event["ip"]][event["user"]] += 1

    return ip_counts, event_counts, failed_logins


def main():
    log_path = Path(__file__).parent / "data" / "auth.log"

    events, corrupted_lines = read_events(log_path)

    ip_counts, event_counts, failed_logins = analyze_events(events)

    print("Total lines:", len(events) + len(corrupted_lines))
    print("Valid lines:", len(events))
    print("Corrupted lines:", len(corrupted_lines))

    print("\nEvents by IP:")
    print(ip_counts)

    print("\nEvents by type:")
    print(event_counts)

    failed_ip_counts = Counter()

    for event in events:
        if event["event"] == "LOGIN_FAILED":
            failed_ip_counts[event["ip"]] += 1

    print("\nTop 3 IPs with failed logins:")
    print(failed_ip_counts.most_common(3))

    print("\nUsers with more than 5 failed logins from one IP:")

    for ip, users in failed_logins.items():
        for user, count in users.items():
            if count > 5:
                print(f"IP: {ip}, User: {user}, Failed logins: {count}")


if __name__ == "__main__":
    main()


# Repeated activity from 203.0.113 IP may indicate suspicious network behavior.