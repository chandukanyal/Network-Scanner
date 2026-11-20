import socket
import ipaddress
from datetime import datetime

# Get target IP from user
target = input("Enter target IP address: ")

# Validate target IP
try:
    ipaddress.ip_address(target)
except ValueError:
    print("Invalid IP address!")
    exit()

# Ports to scan
ports = [
    21, 22, 23, 25, 53, 80, 110, 135, 139,
    443, 445, 3306, 3389, 8080, 8443
]

# Get current date and time
scan_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Initialize report
report = []

report.append("NETWORK SCAN REPORT")
report.append("=" * 40)
report.append(f"Target IP: {target}")
report.append(f"Scan Date: {scan_time}")
report.append("=" * 40)

# Counter for open ports
open_ports = 0

print(f"\nScanning target: {target}\n")

# Scan ports
for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    result = sock.connect_ex((target, port))

    if result == 0:
        open_ports += 1

        try:
            service = socket.getservbyport(port, "tcp")
        except OSError:
            service = "Unknown"

        message = f"Port {port} | OPEN | Service: {service}"

        print(f"[+] {message}")
        report.append(message)

    sock.close()

# Handle no open ports
if open_ports == 0:
    message = "No open ports found in the scanned port list."
    print(message)
    report.append(message)

# Finish report
report.append("=" * 40)
report.append("Scan completed.")
report.append(f"Total open ports: {open_ports}")

# Save report to file
with open("scan_report.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(report))

print("\n" + "=" * 40)
print("Scan completed successfully!")
print(f"Total open ports: {open_ports}")
print("Report saved as scan_report.txt")
