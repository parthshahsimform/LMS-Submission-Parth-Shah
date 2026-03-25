import re
import os
import json
from collections import defaultdict

# Read log file
with open("data_log.txt", "r") as file:
    log_data = file.read()
    lines = log_data.splitlines()

# 1. Extract All IP Addresses

ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
ips = sorted(set(re.findall(ip_pattern, log_data)))

print("Unique IP Addresses:")
print(ips)

# 2. Extract User Actions (INFO logs)

user_actions = defaultdict(set)

info_pattern = r'INFO.*?User\s+([a-zA-Z0-9_]+).*?(UPDATE|created a new record|deleted|login|logout)'

for line in lines:
    match = re.search(info_pattern, line)
    if match:
        username = match.group(1)
        action = match.group(2)
        user_actions[username].add(action)

# Convert sets to lists
user_actions = {user: list(actions) for user, actions in user_actions.items()}

print("\nUser Actions:")
print(user_actions)

# 3. Validate and Extract Email Addresses

email_pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
emails = re.findall(email_pattern, log_data)

print("\nEmail Addresses:")
print(emails)

# 4. Extract Phone Numbers

phone_pattern = r'\b\d{3}-\d{3}-\d{4}\b'
phones = set(re.findall(phone_pattern, log_data))

print("\nPhone Numbers:")
print(phones)

# 5. Extract All URLs

url_pattern = r'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}[^ ]*'
urls = set(re.findall(url_pattern, log_data))

print("\nURLs:")
print(urls)

# 6. Classify Log Levels

levels = ["INFO", "WARNING", "ERROR", "CRITICAL"]
log_counts = {level: 0 for level in levels}

for line in lines:
    for level in levels:
        if re.search(rf'\b{level}\b', line):
            log_counts[level] += 1

print("\nLog Level Counts:")
print(log_counts)

# 7. Extract Timestamps

timestamp_pattern = r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]'
timestamps = sorted(re.findall(timestamp_pattern, log_data))

print("\nTimestamps:")
print(timestamps)

# 8. Mask Sensitive Information

masked_log = log_data

# Mask IP
masked_log = re.sub(ip_pattern, "***.***.***.***", masked_log)

# Mask phone
masked_log = re.sub(phone_pattern, "XXX-XXX-XXXX", masked_log)

# Mask email
masked_log = re.sub(email_pattern, "hidden@example.com", masked_log)

with open("masked_data_log.txt", "w") as file:
    file.write(masked_log)

print("\nMasked log saved to masked_data_log.txt")

# 9. Validate Error Codes

error_pattern = r'\bDB_ERR_\d{4}\b'
error_codes = sorted(set(re.findall(error_pattern, log_data)))

print("\nValid Error Codes:")
print(error_codes)

# 10. Parse Log into Structured Format

parsed_logs = []

log_pattern = r'\[(.*?)\]\s+(INFO|WARNING|ERROR|CRITICAL)\s+(.*)'

for line in lines:
    match = re.match(log_pattern, line)
    if match:
        timestamp, level, message = match.groups()

        parsed_logs.append({
            "timestamp": timestamp,
            "level": level,
            "message": message
        })

with open("parsed_log.json", "w") as file:
    json.dump(parsed_logs, file, indent=4)

print("\nParsed log saved to parsed_log.json")