import socket
import sys
import os
import math

UDP_IP = "127.0.0.1"
UDP_PORT_IN = 8080
# UDP_PORT_OUT = 8081

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((UDP_IP, UDP_PORT_IN))

packetsize = 256

pos = 0

prevdata = b''

while True:
    data, addr = sock.recvfrom(packetsize)
    if data:
        if prevdata != data:
            sizein = len(data)
            print("[recv data]", pos, sizein, "ACCEPTED")
            # print(data)
            message = "[recv ack] " + str(pos)
            sock.sendto(message.encode(), addr)
            prevdata = data
            pos += sizein
        else:
            print("[recv data]", pos - sizein, sizein, "IGNORED")
            # print(data)
            message = "[recv ack] " + str(pos)
            sock.sendto(message.encode(), addr)
    if sizein < packetsize:
        print("[completed]")
        break
