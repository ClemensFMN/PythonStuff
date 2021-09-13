# from https://twistedmatrix.com/documents/current/core/howto/servers.html

# chatserver.py extended by an additional sayto command...
# as client use telnet localhost 8123


from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor
import re

class Chat(LineReceiver):
    def __init__(self, users):
        self.users = users
        self.name = None
        self.state = "GETNAME"

    def connectionMade(self):
        self.sendLine(b"What's your name?")

    def connectionLost(self, reason):
        if self.name in self.users:
            del self.users[self.name]

    def lineReceived(self, line):
        lineu = line.decode("utf-8") # convert the byte array to an utf-8 string
        prsd = re.split(r'\W+', lineu) # split into string separated by spaces
        cmd = prsd[0] # the first chunk is the "command"

        if(cmd == "NAME"): # user defines the name
            data = prsd[1] # this is the name
            print("user with name {} connected".format(data))
            self.users[data] = self # add to user dict
            print(self.users)
            self.sendLine(b"Welcome , " + data.encode('UTF-8'))

        elif(cmd == "LIST"): # see list of connected users
            message = "Current users: " # build up a response by listing all users
            users = self.users.keys()
            print(users)
            message += ", ".join(users)
            self.sendLine(message.encode('UTF-8')) # and send this back to the client who issued the "LIST" command

        elif(cmd == "SAY"): # pub message to all clients (including ourselves)
            for name, protocol in self.users.items():
                # source = u"<{}> ".format(self.transport.getHost()).encode("ascii")
                msg = name + ": " + line
                protocol.sendLine(msg.encode('UTF-8'))
                # send only to the other clients
                #if c != self: 
                #    source = u"<{}> ".format(self.transport.getHost()).encode("ascii")
                #    c.sendLine(source + line)
        elif(cmd == "SAYTO"): # send msg to specific client
            to = prsd[1] # recipient
            protocol = self.factory.users.get(to)
            if(protocol == None): # recipient not found 
                self.sendLine(b"recipient not found")
            else: # recipient found
                print(protocol)
                source = u"<{}> ".format(self.transport.getHost()).encode("ascii")
                protocol.sendLine(source + line) # -> send message
        else:
            print("unknown command")

class ChatFactory(Factory):
    def __init__(self):
        self.users = {}  # maps user names to Chat instances

    def buildProtocol(self, addr):
        return Chat(self.users)


reactor.listenTCP(8123, ChatFactory())
reactor.run()
