# Hackhoven's ping_sweeper

import sys
import subprocess
import platform
import concurrent.futures
import ipaddress
import logging

def ping_sweeper(ip):
    if platform.system().lower() == 'windows':
        cmd = ['ping', '-n', '1', '-w', '1000']  # 1 second timeout for Windows
    else:
        cmd = ['ping', '-c', '1', '-W', '1']     # 1 second timeout for Unix-like systems

    try:
        result = subprocess.run(cmd + [str(ip)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if "Destination host unreachable" in result.stdout:
            return
        else:
            logging.info(f"The host {ip} is up.")

    except subprocess.CalledProcessError as e:
        logging.error(f"Error occurred with {ip}: {e}")

def main():
    logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

    if len(sys.argv) != 2:
        print("Usage: python3 ping_sweeper.py <IP range>")
        sys.exit(1)

    ip_range = sys.argv[1]

    try:
        network = ipaddress.ip_network(ip_range)
    except ValueError as e:
        print("Invalid IP range:", e)
        sys.exit(1)

    with concurrent.futures.ThreadPoolExecutor(max_workers=32) as executor:
        for ip in network.hosts():
            executor.submit(ping_sweeper, ip)

if __name__ == "__main__":
    main()

