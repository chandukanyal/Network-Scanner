import socket

target = "127.0.0.1"

ports = [
    21, 22, 23, 25, 53, 80, 110, 135, 139,
    443, 445, 3306, 3389, 8080, 8443
]

print(f"Scanning target: {target}")
print("-" * 40)

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"[+] Port {port} is OPEN")

    sock.close()

print("-" * 40)
print("Scan completed.")