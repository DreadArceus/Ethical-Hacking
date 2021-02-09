#!/usr/bin/python3.9
import sys
import socket
from datetime import datetime

def make_pretty(x: str) -> str:
    num = 50 - len(x)
    return '-' * (num // 2) + x + '-' * (num // 2 + num % 2)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Give correct arguments, weirdchamp')
        sys.exit()
    results = {'open_ports': []}
    try:
        target = socket.gethostbyname(sys.argv[1])
        print(make_pretty(f'Scanning target: {target}'))
        print(make_pretty(f'Start Time: {datetime.now()}'))
        for port in range(50, 85):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1.069)
            print(f'Checking Port {port}...')
            result = s.connect_ex((target, port))
            if result == 0:
                results['open_ports'].append(port)
                print(f'Port {port} is open')
            s.close()
    except KeyboardInterrupt:
        print(f'\n{make_pretty("Script stopped by keyboard")}')
        sys.exit()
    except socket.gaierror:
        print(f'Unable to resolve hostname')
        sys.exit()
    except socket.error:
        print(f'Unable to connect to the server')
        sys.exit()
    print(make_pretty(f'End Time: {datetime.now()}'))
    print(make_pretty('RESULTS'))
    print('Open Ports:', *results['open_ports'])
