from twisted.internet import reactor, protocol, endpoints
from twisted.protocols import basic
import re

# simple example from the homepage https://www.twistedmatrix.com/trac/
# added own extensions

class PubProtocol(basic.LineReceiver):
    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        # self.factory.clients.add(self)
        print("Connection from {}".format(self))

    def connectionLost(self, reason):
        self.factory.clients.remove(self)

    def lineReceived(self, line):
        lineu = line.decode("utf-8")
        prsd = re.split(r'\W+', lineu)
        cmd = prsd[0]
        
        if(cmd == "NAME"):
            data = prsd[1]
            print("client with name {} connected".format(data))
            self.factory.clients[data] = self
            print(self.factory.clients)
        elif(cmd == "LIST"):
            print(self.factory.clients)
        elif(cmd == "SAY"):
            for name, protocol in self.factory.clients.items():
                source = u"<{}> ".format(self.transport.getHost()).encode("ascii")
                protocol.sendLine(source + line)
                # send only to the others
                #if c != self: 
                #    source = u"<{}> ".format(self.transport.getHost()).encode("ascii")
                #    c.sendLine(source + line)
        elif(cmd == "SAYTO"):
            to = prsd[1]
            protocol = self.factory.clients.get(to)
            if(protocol == None):
                self.sendLine(b"recipient not found")
            else:
                print(protocol)
                source = u"<{}> ".format(self.transport.getHost()).encode("ascii")
                protocol.sendLine(source + line)
        else:
            print("unknown command")


                
class PubFactory(protocol.Factory):
    def __init__(self):
        self.clients = {}

    def buildProtocol(self, addr):
        return PubProtocol(self)

endpoints.serverFromString(reactor, "tcp:1025").listen(PubFactory())
reactor.run()
