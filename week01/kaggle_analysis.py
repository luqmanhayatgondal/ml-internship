from pathlib import Path
import csv
from collections import Counter


def load_kaggle_data():
    """Load the Kaggle system logs CSV file."""
    file_path = Path(__file__).parent / "data" / "System logs kaggle.csv"

    with file_path.open("r", encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def analyze_logs(records):
    """Analyze log levels and authentication failures."""
    log_levels = Counter()
    auth_failures = 0
    ssh_logs = 0
    ftp_logs = 0
    kernel_logs = 0

    for record in records:
        log_levels[record["log_level"]] += 1

        message = record["message"].lower()

        if "authentication failure" in message:
            auth_failures += 1

        if "sshd" in message:
            ssh_logs += 1

        if "ftp" in message:
            ftp_logs += 1

        if "kernel" in message:
            kernel_logs += 1

    return (log_levels, auth_failures, ssh_logs, ftp_logs, kernel_logs)


def main():
    records = load_kaggle_data()

    log_levels, auth_failures, ssh_logs, ftp_logs, kernel_logs = analyze_logs(records)

    print("KAGGLE SYSTEM LOG ANALYSIS")
    print("==========================")

    print("\nTotal records:", len(records))

    print("\nRecords by log level:")
    print(log_levels)

    print("\nAuthentication failures:", auth_failures)
    print("SSH related logs:", ssh_logs)
    print("FTP related logs:", ftp_logs)
    print("Kernel related logs:", kernel_logs)


if __name__ == "__main__":
    main()
