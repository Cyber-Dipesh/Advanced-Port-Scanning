This is a lightweight, multithreaded port scanner written in Python 3. It allows users to quickly scan multiple TCP ports on a target host and identify which ones are open or closed.

## 🔧 Features
- Fast multithreaded scanning
- Hostname and IP resolution
- Timeout handling for unreachable ports
- Clean CLI interface using `argparse`

## 🚀 Usage
```bash
python port_scanner.py -H <target_host> -p <port1,port2,...>
Example :
        python port_scanner.py -H scanme.nmap.org -p 22,80,443
