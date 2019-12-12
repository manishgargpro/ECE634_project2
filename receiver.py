import socket
import sys
import os
import math

UDP_IP = "127.0.0.1"
UDP_PORT_IN = 8080
# UDP_PORT_OUT = 8081

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((UDP_IP, UDP_PORT_IN))

packetsize = 32

pos = 0

prevdata = ""

while True:
    packet, addr = sock.recvfrom(packetsize+4)
    if packet:
        sizein = len(packet) - 4
        data = packet.decode()[0:sizein]
        checksum = 0
        for i in data:
            checksum += ord(i)
        checksumin = packet.decode()[sizein:len(packet)]
        if prevdata != data:
            if int(checksumin) == checksum:
                print("[recv data]", pos, len(data), "ACCEPTED")
                # print(data, checksumin)
                message = "[recv ack] " + str(pos)
                sock.sendto(message.encode(), addr)
                prevdata = data
                pos += sizein
        else:
            print("[recv data]", pos - packetsize, sizein, "IGNORED")
            # print(data)
            message = "[recv ack] " + str(pos)
            sock.sendto(message.encode(), addr)
    if sizein < packetsize:
        print("[completed]")
        break
