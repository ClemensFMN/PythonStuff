# from https://twistedmatrix.com/documents/current/core/howto/servers.html

# a simple chat server. you need to provide your name first.
# then you can list all users & say something to everyone
# as client use telnet localhost 8123


from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor


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
        if self.state == "GETNAME":
            self.handle_GETNAME(line)
        else:
            self.handle_CHAT(line)

    def handle_GETNAME(self, name):
        if name in self.users:
            self.sendLine(b"Name taken, please choose another.")
            return
        self.sendLine(b"Welcome, " + name)
        self.name = name
        self.users[name] = self
        self.state = "CHAT"
        print(self.users)

    def handle_CHAT(self, message):
        if(message == b"LIST"): # we define a command which lists all users
            message = b"Current users: " # build up a response by listing all users
            users = self.users.keys()
            message += b", ".join(users)
            self.sendLine(message) # and send this back to the client who issued the "LIST" command
        else:
            message = self.name + b": " + message # otherwise we simply send what we received to all other clients
            for name, protocol in self.users.items():
                if protocol != self:
                    protocol.sendLine(message)


class ChatFactory(Factory):
    def __init__(self):
        self.users = {}  # maps user names to Chat instances

    def buildProtocol(self, addr):
        return Chat(self.users)


reactor.listenTCP(8123, ChatFactory())
reactor.run()
