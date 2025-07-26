import os
from datetime import datetime
from random import choice, randint

verbs = ["Fix", "Add", "Improve", "Refactor", "Remove", "Optimize"]
objects = ["logging", "API handler", "core logic", "utils", "data parser"]
contexts = ["in main flow", "in config", "in commit generator", "for log.txt", "in script"]

def generate_commit_message():
    return f"{choice(verbs)} {choice(objects)} {choice(contexts)}"

def simulate_log_entry():
    now = datetime.now().isoformat(timespec='seconds')
    entry = f"[AUTO LOG] {now} {randint(1000,9999)}"
    with open("log.txt", "a") as log:
        log.write(entry + "\n")
    return entry

if __name__ == "__main__":
    print("🔧 Simulating commit...")
    print("📄 Log entry:", simulate_log_entry())
    print("📝 Commit message:", generate_commit_message())
