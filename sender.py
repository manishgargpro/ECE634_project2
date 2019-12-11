import socket
import sys
import os
import math

UDP_IP = sys.argv[1]
UDP_PORT_OUT = int(sys.argv[2])
UDP_PORT_IN = 8081
filename = sys.argv[3]

filestats = os.stat(filename)

packetsize = 32

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((UDP_IP, UDP_PORT_IN))

with open(filename, "rb") as f:
    packet = f.read(packetsize)
    while packet:
        sizeout = len(packet)
        pos = f.tell()
        print("[send data]", pos - sizeout, sizeout)
        sock.sendto(packet, (UDP_IP, UDP_PORT_OUT))
        data, addr = sock.recvfrom(32)
        if data:
            print(data.decode())
            packet = f.read(packetsize)
        else:
            print("[resend data]", pos - sizeout, sizeout)
            # sock.sendto(packet, (UDP_IP, UDP_PORT_OUT))
    print("[completed]")
