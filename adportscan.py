#!/usr/bin/env python3

import socket
import argparse
from threading import Thread


def conn_scan(tgt_host, tgt_port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((tgt_host, tgt_port))
        print(f"[+] {tgt_port}/tcp Open")
    except (socket.timeout, socket.error):
        print(f"[-] {tgt_port}/tcp Closed")
    finally:
        sock.close()


def port_scan(tgt_host, tgt_ports):
    try:
        tgt_ip = socket.gethostbyname(tgt_host)
    except socket.gaierror:
        print(f"[!] Unknown Host: {tgt_host}")
        return

    try:
        tgt_name = socket.gethostbyaddr(tgt_ip)[0]
        print(f"[+] Scan Results for: {tgt_name} ({tgt_ip})")
    except socket.herror:
        print(f"[+] Scan Results for: {tgt_ip}")

    for tgt_port in tgt_ports:
        thread = Thread(target=conn_scan, args=(tgt_host, tgt_port))
        thread.start()


def main():
    parser = argparse.ArgumentParser(description="Advanced Port Scanner")
    parser.add_argument("-H", "--host", required=True, help="Target host")
    parser.add_argument("-p", "--ports", required=True, help="Comma-separated list of target ports")

    args = parser.parse_args()
    tgt_host = args.host
    tgt_ports = [int(port.strip()) for port in args.ports.split(",")]

    port_scan(tgt_host, tgt_ports)

if __name__ == "__main__":
    main()
