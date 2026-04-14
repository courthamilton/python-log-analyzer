import re
from collections import Counter

with open("sample.log", "r") as file:
    logs = file.readlines()

ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
status_pattern = r'"\s(\d{3})\s'

ips = []
status_codes = []

for line in logs:
    ip_match = re.search(ip_pattern, line)
    status_match = re.search(status_pattern, line)

    if ip_match:
        ips.append(ip_match.group())

    if status_match:
        status_codes.append(status_match.group(1))

ip_counts = Counter(ips)
status_counts = Counter(status_codes)

print("\nTop 5 IP Addresses:")
for ip, count in ip_counts.most_common(5):
    print(f"{ip}: {count}")

print("\nHTTP Status Codes:")
for code, count in status_counts.items():
    print(f"{code}: {count}")

print("\nSuspicious IPs (more than 5 requests):")
for ip, count in ip_counts.items():
    if count > 5:
        print(f"{ip}: {count} requests")