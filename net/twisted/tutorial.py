# based on https://twistedmatrix.com/documents/current/core/howto/tutorial/intro.html

from twisted.internet import protocol, reactor, endpoints
from twisted.protocols import basic


class MyProtocol(basic.LineReceiver):
    def lineReceived(self, data):
        print("Received")
        print(data)
        self.transport.write(b"Received\r\n")
        self.transport.write(data)
        self.transport.loseConnection()


class MyFactory(protocol.ServerFactory):
    protocol = MyProtocol


mPEndpoint = endpoints.serverFromString(reactor, "tcp:1079")
mPEndpoint.listen(MyFactory())
reactor.run()