# Network Tool

## Overview

`network_tool.py` is a Python script for automating common network management tasks on a Linux system. It provides functionality for managing IP addresses, configuring firewall rules, and monitoring network performance.

## Dependencies

- Python 3
- `psutil` library

## Installation

1. **Clone the repository** (or save the script to your local machine):
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Install `psutil`**:
    ```bash
    pip3 install psutil
    ```

3. **Ensure the script is executable**:
    ```bash
    chmod +x network_tool.py
    ```

## Usage

Run the script using Python 3 and `sudo` for necessary privileges. Below are the commands and their descriptions:

### IP Address Management

#### Add an IP Address
```bash
sudo python3 network_tool.py ip add <interface> <ip_address>
```
```bash
sudo python3 network_tool.py ip add eth0 192.168.1.10/24
```
#### Delete an IP Address
```bash
sudo python3 network_tool.py ip delete <interface> <ip_address
```
```bash
sudo python3 network_tool.py ip delete eth0 192.168.1.10/24
```
#### Show IP Addresses
```bash
python3 network_tool.py ip show
```
#### Firewall Management
Add a Firewall Rule
```bash
sudo python3 network_tool.py firewall add "<rule>"
```
```bash
sudo python3 network_tool.py firewall add "-A INPUT -p tcp --dport 22 -j ACCEPT"
```
Delete a Firewall Rule
```bash
sudo python3 network_tool.py firewall delete "<rule>"
```
```bash
sudo python3 network_tool.py firewall delete "-D INPUT -p tcp --dport 22 -j ACCEPT"
```
List Firewall Rules
```bash
sudo python3 network_tool.py firewall list
```
#### Network Performance Monitoring
```bash
python3 network_tool.py monitor
```
#### Allow Incoming SSH Connections
```bash
sudo python3 network_tool.py firewall add "-A INPUT -p tcp --dport 22 -j ACCEPT"
```
#### Block Incoming HTTP Connections
```bash
sudo python3 network_tool.py firewall add "-A INPUT -p tcp --dport 80 -j DROP"
```
#### Allow Outgoing DNS Requests
```bash
sudo python3 network_tool.py firewall add "-A OUTPUT -p udp --dport 53 -j ACCEPT"
```
#### Monitor Network Performance
```bash
python3 network_tool.py monitor
```
#### Logging
The script logs its actions to a file named network_tool.log in the same directory. You can check this file to review the execution logs.
