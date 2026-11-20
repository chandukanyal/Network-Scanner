import socket
import ipaddress

# Get target IP from user
target = input("Enter target IP address: ")

# Validate IP address
try:
    ipaddress.ip_address(target)
except ValueError:
    print("Invalid IP address!")
    exit()

ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 443, 445, 3306, 3389, 8080, 8443]

print(f"\nScanning {target}")
print("=" * 50)

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    result = sock.connect_ex((target, port))

    if result == 0:
        try:
            service = socket.getservbyport(port, "tcp")
        except OSError:
            service = "Unknown"

        print(f"[+] Port {port:<5} OPEN   Service: {service}")

    sock.close()

print("=" * 50)
print("Scan completed.")
