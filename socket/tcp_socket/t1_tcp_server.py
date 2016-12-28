# -*- coding: UTF-8 -*-

from socket import *
from time import ctime

HOST = ''    # 任何可用的地址
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpServerSock = socket(AF_INET, SOCK_STREAM)
tcpServerSock.bind(ADDR)
tcpServerSock.listen(5)

while True:
    print 'waiting for connection...'
    tcpClientSock, addr = tcpServerSock.accept()
    print '...connected from:', addr

    while True:
        data = tcpClientSock.recv(BUFSIZE)
        if not data:
            break
        tcpClientSock.send('[%s] %s' % (ctime(), data))

    tcpClientSock.close()

tcpServerSock.close()  ## Never hit