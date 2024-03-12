# Hackhoven's ping sweeper

This is a simple Python script designed to quickly scan a range of IP addresses to determine which hosts are online and reachable via ICMP ping requests. This tool is useful for network administrators and security professionals to identify active hosts within a given IP range.

## Features

- **Platform Agnostic:** The script is designed to work on both Windows and Unix-based systems, utilizing platform-specific commands for ICMP ping requests.
- **Simple Usage:** Users can specify an IP range as a command-line argument to scan for active hosts.
- **Fast and Efficient:** The script uses subprocesses to execute ping requests in parallel, allowing for rapid scanning of IP addresses.

## Usage

To use the Ping Sweeper, follow these steps:

1. Open a terminal or command prompt.
2. Clone this repository to your local machine: `git clone https://github.com/Hackhoven/python_ping_sweeper.git`
3. Navigate to the directory containing the script: `cd Hackhoven/python_ping_sweeper`
4. Run the script using the command `python3 ping_sweeper.py <IP range>`, where `<IP range>` specifies the range of IP addresses to scan (e.g., `192.168.1`).
5. View the output to identify online and offline hosts within the specified IP range.

Enjoy using my simple ping sweeper to quickly scan your network for active hosts!
