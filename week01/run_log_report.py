import sys
from collections import Counter
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

    # Count events by IP and event type
    ip_counts = Counter(event.ip for event in events)
    event_counts = Counter(event.event for event in events)

    # Find failed login events
    failed_events = [event for event in events if event.event == "LOGIN_FAILED"]

    # Count failed logins by IP
    failed_ip_counts = Counter(event.ip for event in failed_events)

    # Count failed logins by IP and user
    failed_user_counts = Counter((event.ip, event.user) for event in failed_events)

    print("Total lines:", len(events) + len(bad_lines))
    print("Total valid events:", len(events))
    print("Corrupted lines:", len(bad_lines))
    print("CSV records:", len(loader.load_csv("sample.csv")))

    print("\nEvents by IP:")
    print(ip_counts)

    print("\nEvents by type:")
    print(event_counts)

    print("\nTop 3 IPs with failed logins:")
    print(failed_ip_counts.most_common(3))

    print("\nUsers with more than 5 failed logins from one IP:")

    found_users = False

    for (ip, user), count in failed_user_counts.items():
        if count > 5:
            print(f"IP: {ip}, User: {user}, Failed logins: {count}")
            found_users = True

    if not found_users:
        print("No users found.")


if __name__ == "__main__":
    main()
