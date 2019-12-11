import socket
import sys
import os
import math

UDP_IP = "127.0.0.1"
UDP_PORT = 80

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((UDP_IP, UDP_PORT))

packetsize = 32

pos = 0

while True:
    try:
        data, addr = sock.recvfrom(packetsize)
        if data:
            sizein = len(data)
            print("[recv data]", pos, sizein, "accepted")
            pos += sizein
        else:
            exit(1)
    except KeyboardInterrupt:
        exit(1)
