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

las = 0

while True:
    packet, addr = sock.recvfrom(packetsize+16)
    if packet:
        packetd = packet.decode().split(',')
        data = packetd[0]
        checksumin = int(packetd[1])
        posin = int(packetd[2])
        # print(data, checksumin, posin, pos, las)
        sizein = len(data)
        checksum = 0
        for i in data:
            checksum += ord(i)
        if posin == pos:
            if int(checksumin) == checksum:
                print("[recv data]", pos, len(data), "ACCEPTED")
                message = "[recv ack]," + str(pos)
                sock.sendto(message.encode(), addr)
                las = pos
                pos += sizein
        elif posin == las:
            print("[recv data]", pos, len(data), "IGNORED")
            message = "[recv ack], " + str(las)
            sock.sendto(message.encode(), addr)
        else:            
            print("[recv data]", pos - packetsize, sizein, "IGNORED")
    if sizein < packetsize:
        print("[completed]")
        break
