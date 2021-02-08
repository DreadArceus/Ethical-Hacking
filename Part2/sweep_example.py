#!/usr/bin/python3

import subprocess
import datetime
import re
import argparse

def write_result(filename, ping):
    with open(filename, "w") as f:
        f.write(f'Start time {datetime.datetime.now()}\n')
        for result in ping:
            f.write(result)
        f.write(f'End time {datetime.datetime.now()}\n')

def ping_subnet(socket):
    for addr in range(1, 255):
        yield subprocess.Popen(["ping", f'{socket}.{addr}', "-c", "1"], \
                stdout=subprocess.PIPE).stdout.read().decode()

def main(subnet, filename):
    write_result(filename, ping_subnet(subnet))

def parse_arguments():
    parser = argparse.ArgumentParser(usage='')
    parser.add_argument('subnet', type=str)
    parser.add_argument('-f', '--filename', type=str)
    args = parser.parse_args()

    return args.subnet, args.filename
    
if __name__ == '__main__':
    main(*parse_arguments())
