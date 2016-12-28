# -*- coding: UTF-8 -*-

from twisted.internet import protocol, reactor
from time import ctime

PORT = 21567

class TSServerProtocol(protocol.Protocol):
    def connectionMade(self):
        client = self.client = self.transport.getPeer().host
        print '...connected from:', client

    def dataReceived(self, data):
        self.transport.write('[%s] %s' %(ctime(), data))


factory = protocol.Factory()
factory.protocol = TSServerProtocol
print 'waiting from connection...'
reactor.listenTCP(PORT, factory)
reactor.run()