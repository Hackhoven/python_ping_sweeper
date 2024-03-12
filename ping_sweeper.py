# Hackhoven's simple ping sweeper

import sys
import subprocess
import platform

def ping_sweeper(ip_range):

    if platform.system().lower() == 'windows':
        cmd = ['ping', '-n', '1']
    else:
        cmd = ['ping', '-c', '1']

    
    for i in range(1, 255):
        ip = f"{ip_range}.{i}"
        cmd.append(ip)

        try:
            result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            if "Destination host unreachable" in result.stdout:
                print(f"The host {ip} is down.")
            else:
                print(f"The host {ip} is up.")
        
        except subprocess.CalledProcessError:
            print(f"Error occured with {ip}")

        cmd.pop()


def main():

    if len(sys.argv) != 2:
        print("Run python3 ping_sweeper.py <IP range>")
        sys.exit(1)

    ip_range = sys.argv[1]

    ping_sweeper(ip_range)


if __name__ == "__main__":
    main()
