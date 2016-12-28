# -*- coding: UTF-8 -*-

from socket import *
from time import ctime

HOST = ''    # 任何可用的地址
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpServerSock = socket(AF_INET, SOCK_DGRAM)
udpServerSock.bind(ADDR)

while True:
    print 'waiting for message...'
    data, addr = udpServerSock.recvfrom(BUFSIZE)

    udpServerSock.sendto('[%s] %s' % (ctime(), data), addr)

    print '...received from and return to:', addr

udpServerSock.close()   ## Never hit
