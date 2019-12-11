import socket
import sys
import os
import math
import signal
import time

UDP_IP = sys.argv[1]
UDP_PORT_OUT = int(sys.argv[2])
UDP_PORT_IN = 8081

filename = sys.argv[3]

filestats = os.stat(filename)

packetsize = 256

timeout = 200    #in milliseconds

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((UDP_IP, UDP_PORT_IN))

sock.settimeout(timeout/1000)

def sendpacket(p, pos, st):
    sock.sendto(packet, (UDP_IP, UDP_PORT_OUT))
    print(st, pos - sizeout, sizeout)

with open(filename, "rb") as f:
    packet = f.read(packetsize)
    while packet:
        sizeout = len(packet)
        pos = f.tell()
        sendpacket(packet, pos, "[send data]")
        ack = {}
        while ack == {}:
            try:
                ack, addr = sock.recvfrom(32)
                if ack:
                    print(ack.decode())
                    packet = f.read(packetsize)
            except socket.timeout:
                sendpacket(packet, pos, "[resend data]")
    print("[completed]")
