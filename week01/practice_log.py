from pathlib import Path

data_folder = Path(__file__).parent / "data"
data_folder.mkdir(exist_ok=True)

file_path = data_folder / "auth_practice.log"

lines = []

events = ["LOGIN_SUCCESS", "LOGIN_FAILED", "LOGOUT", "PASSWORD_CHANGE"]
ips = ["192.168.1.10", "10.0.0.7", "203.0.113.45", "192.168.1.20"]
users = ["root", "admin", "test", "luqman"]

for i in range(400):
    timestamp = f"2026-11-02T08:{i // 60:02d}:{i % 60:02d}Z"
    ip = ips[i % len(ips)]
    event = events[i % len(events)]
    user = users[i % len(users)]

    lines.append(f"{timestamp} {ip} {event} user={user}")

lines.extend(
    [
        "### corrupted entry ###",
        "this is not a valid log line",
        "2026-11-02 invalid timestamp",
    ]
)

file_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

print("Practice log created!")
print(f"Total lines: {len(lines)}")
print("Valid lines: 400")
print("Corrupted lines: 3")
