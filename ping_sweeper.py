# Hackhoven's ping_sweeper

import sys
import subprocess
import concurrent.futures
import platform
import ipaddress
import logging


def ping_sweeper(ip):
    if platform.system().lower() == "windows":
        cmd = ['ping', '-n', '1', '-w', '1000']
    else:
        cmd = ['ping', '-c', '1', '-W', '1']

    try:
        result = subprocess.run(cmd + [str(ip)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if "Destination host unreachable" not in result.stdout:
            logging.info(f"The host {ip} is up.")
    
    except subprocess.CalledProcessError: 
        pass    # Suppress error messages for unreachable hosts

    
def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    if len(sys.argv) != 2:
        print("Command usage: python3 ping_sweeper.py <network ip address>")
        sys.exit(1)

    net_ip_address = sys.argv[1]  #192.168.100.0/24

    try:
        network = ipaddress.ip_network(net_ip_address)    #192.168.100.0-255
    except ValueError as e:
        print("Invalid IP range: ", e)
        sys.exit(1)

    with concurrent.futures.ThreadPoolExecutor(max_workers=32) as executor:
        for ip in network.hosts():
            executor.submit(ping_sweeper, ip)

if __name__ == "__main__":
    main()
