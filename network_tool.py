#!/usr/bin/env python3
import os
import psutil
import subprocess
import argparse
import logging

# set up logging
logging.basicConfig(filename='network_tool.log', level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")


def run_command(command):
    try:
        result = subprocess.run(command, check=True, text=True, shell=True, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        logging.info(f"Command '{command}' executed successfully")
        return result.stdout
    except subprocess.CalledProcessError as e:
        logging.error(f"Command '{command}' failed with error: {e.stderr}")
        return None


def add_ip_address(interface, ip_address):
    command = f"sudo ip addr add {ip_address} dev {interface}"
    return run_command(command)


def delete_ip_address(interface, ip_address):
    command = f"sudo ip addr del {ip_address} dev {interface}"
    return run_command(command)


def show_ip_address():
    command = "ip addr show"
    return run_command(command)


# firewall configuration
def add_firewall_rule(rule):
    command = f"sudo iptables {rule}"
    return run_command(command)


def delete_firewall_rule(rule):
    command = f"sudo iptables {rule}"
    return run_command(command)


def list_firewall_rules():
    command = f"sudo iptables -L"
    return run_command(command)


# Network Performance Monitoring
def monitor_network():
    net_io = psutil.net_io_counters(pernic=True)
    for interface, stats in net_io.items():
        print(f"Interface: {interface} ")
        print(f"      Byte Sent: {stats.bytes_sent} ")
        print(f"      Bytes Received: {stats.bytes_recv}")


# CLI
def main():
    parser = argparse.ArgumentParser(description="Linux Networking Automation Tool")
    subparsers = parser.add_subparsers(dest="command")

    # IP address commands
    ip_parser = subparsers.add_parser("ip", help="Manage IP addresses")
    ip_subparsers = ip_parser.add_subparsers(dest="action")

    add_ip_parser = ip_subparsers.add_parser("add", help="Add Ip address")
    add_ip_parser.add_argument("interface", type=str, help="Network interface")
    add_ip_parser.add_argument("ip_address", type=str, help="IP address")

    del_ip_parser = ip_subparsers.add_parser("delete", help="Delete IP address")
    del_ip_parser.add_argument("interface", type=str, help="Network interface")
    del_ip_parser.add_argument("ip_address", type=str, help="IP address")

    show_ip_parser = ip_subparsers.add_parser("show", help="Show IP addresses")

    # Firewall Commands
    fw_parser = subparsers.add_parser("firewall", help="Configure firewall")
    fw_subparsers = fw_parser.add_subparsers(dest="action")

    add_fw_parser = fw_subparsers.add_parser("add", help="Add firewall rule")
    add_fw_parser.add_argument("rule", type=str, help="Firewall rule")

    del_fw_parser = fw_subparsers.add_parser("delete", help="Delete firewall rule")
    del_fw_parser.add_argument("rule", type=str, help="Firewall rule")

    list_fw_parser = fw_subparsers.add_parser("list", help="List firewall rules")

    # Network Monitoring Command
    monitor_parser = subparsers.add_parser("monitor", help="Monitor network performance")

    args = parser.parse_args()
    if args.command == "ip":
        if args.action == "add":
            add_ip_address(args.interface, args.ip_address)
        elif args.action == "delete":
            delete_ip_address(args.interface, args.ip_address)
        elif args.action == "show":
            print(show_ip_address())
    
    elif args.command == "firewall":
        if args.action == "add":
            add_firewall_rule(args.rule)
        elif args.action == "delete":
            delete_firewall_rule(args.rule)
        elif args.action == "list":
            print(list_firewall_rules())

    elif args.command == "monitor":
        monitor_network()

if __name__ == "__main__":
    main()