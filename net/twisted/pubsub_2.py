from twisted.internet import reactor, protocol, endpoints
from twisted.protocols import basic
import re

# simple example from the homepage https://www.twistedmatrix.com/trac/
# added own extensions

class PubProtocol(basic.LineReceiver):
    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        print("Connection from {}".format(self)) # log that someone connected

    def connectionLost(self, reason):
        # self.factory.clients.pop(self) TODO: make working

    def lineReceived(self, line):
        lineu = line.decode("utf-8") # convert the byte array to an utf-8 string
        prsd = re.split(r'\W+', lineu) # split into string separated by spaces
        cmd = prsd[0] # the first chunk is the "command"
        
        if(cmd == "NAME"): # client defines the name
            data = prsd[1] # this is the name
            print("client with name {} connected".format(data))
            self.factory.clients[data] = self # add to client dict
            # print(self.factory.clients)
        elif(cmd == "LIST"): # see list of connected clients
            print(self.factory.clients) # TODO: send back to client
        elif(cmd == "SAY"): # pub message to all clients (including ourselves)
            for name, protocol in self.factory.clients.items():
                source = u"<{}> ".format(self.transport.getHost()).encode("ascii")
                protocol.sendLine(source + line)
                # send only to the other clients
                #if c != self: 
                #    source = u"<{}> ".format(self.transport.getHost()).encode("ascii")
                #    c.sendLine(source + line)
        elif(cmd == "SAYTO"): # send msg to specific client
            to = prsd[1] # recipient
            protocol = self.factory.clients.get(to)
            if(protocol == None): # recipient not found 
                self.sendLine(b"recipient not found")
            else: # recipient found
                print(protocol)
                source = u"<{}> ".format(self.transport.getHost()).encode("ascii")
                protocol.sendLine(source + line) # -> send message
        else:
            print("unknown command")


                
class PubFactory(protocol.Factory):
    def __init__(self):
        self.clients = {}

    def buildProtocol(self, addr):
        return PubProtocol(self)

endpoints.serverFromString(reactor, "tcp:1025").listen(PubFactory())
reactor.run()
