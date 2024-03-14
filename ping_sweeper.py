# Hackhoven's ping_sweeper

import sys
import subprocess
import platform
import concurrent.futures

def ping_sweeper(ip):
    if platform.system().lower() == 'windows':
        cmd = ['ping', '-n', '1']
    else:
        cmd = ['ping', '-c', '1']

    try:
        result = subprocess.run(cmd + [ip], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if "Destination host unreachable" in result.stdout:
            return
        else:
            print(f"The host {ip} is up.")

    except subprocess.CalledProcessError:
        print(f"Error occurred with {ip}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 ping_sweeper.py <IP range>")
        sys.exit(1)

    ip_range = sys.argv[1]

    with concurrent.futures.ThreadPoolExecutor(max_workers=64) as executor:
        ips = [f"{ip_range}.{i}" for i in range(1, 255)]
        executor.map(ping_sweeper, ips)

if __name__ == "__main__":
    main()
