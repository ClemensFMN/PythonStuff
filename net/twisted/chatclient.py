from twisted.internet.protocol import Protocol, ClientFactory
from twisted.internet import reactor


class ChatClient(Protocol):
    
    def connectionMade(self):
        self.transport.write(b"Susi\r\n")
    
    def dataReceived(self, data):
        print(data)
        # if we uncomment the following line, we run into an infinite loop; as every send
        # triggers an answer from the server which again calls this function and so on :-)
        # we need some kind of state machine which 
        self.transport.write(b"LIST\r\n")




class ChatClientFactory(ClientFactory):
    #def startedConnecting(self, connector):
    #    print('Started to connect.')

    def buildProtocol(self, addr):
    #    print('Connected.')
        return ChatClient()

    def clientConnectionLost(self, connector, reason):
        print('Lost connection.  Reason:', reason)

    def clientConnectionFailed(self, connector, reason):
        print('Connection failed. Reason:', reason)

reactor.connectTCP("127.0.0.1", 8123, ChatClientFactory())
reactor.run()
