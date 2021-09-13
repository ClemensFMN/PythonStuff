from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class Echo(DatagramProtocol):

    def datagramReceived(self, data, addr):
        print("received %r from %s" % (data, addr))
        # self.transport.write(data, addr)

reactor.listenUDP(5060, Echo())
reactor.run()

# run the script
# in another terminal, execute
# nc -u 127.0.0.1 5060
# enter something and press Enter
# then you should see this in the python script window...
