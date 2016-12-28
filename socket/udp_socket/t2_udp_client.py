# -*- coding: UTF-8 -*-

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpClientSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = raw_input('> ')
    if not data:
        break

    udpClientSock.sendto(data, ADDR)
    data, ADDR = udpClientSock.recvfrom(BUFSIZE)

    if not data:
        break

    print data

udpClientSock.close()