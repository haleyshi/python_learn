# -*- coding: UTF-8 -*-

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

while True:
    data = raw_input('> ')
    if not data:
        break
    tcpClientSock = socket(AF_INET, SOCK_STREAM)  # 每次发送创建新的连接
    tcpClientSock.connect(ADDR)
    tcpClientSock.send('%s\r\n' % data)
    data = tcpClientSock.recv(BUFSIZE)
    if not data:
        break
    print data.strip()

    tcpClientSock.close()