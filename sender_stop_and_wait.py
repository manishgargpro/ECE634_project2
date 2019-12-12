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

packetsize = 32

timeout = 200    #in milliseconds

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((UDP_IP, UDP_PORT_IN))

sock.settimeout(timeout/1000)

def sendpacket(p, pos, st):
    checksum = 0
    for i in p:
        checksum += ord(i)
    pack = p + str(checksum)
    sock.sendto(pack.encode(), (UDP_IP, UDP_PORT_OUT))
    print(st, pos - len(p), len(p))
    # print(pack)


with open(filename, "r") as f:
    packet = f.read(packetsize)
    while packet:
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
