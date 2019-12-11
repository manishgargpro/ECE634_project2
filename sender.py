import socket
import sys
import os
import math

UDP_IP = sys.argv[1]
UDP_PORT = int(sys.argv[2])
filename = sys.argv[3]

filestats = os.stat(filename)

packetsize = 32

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


with open(filename, "rb") as f:
    packet = f.read(packetsize)
    while packet:
        sizeout = len(packet)
        pos = f.tell()
        print("[send data]", pos - sizeout, sizeout)
        sock.sendto(packet, (UDP_IP, UDP_PORT))
        packet = f.read(packetsize)
