import socket
import struct
import binascii


proto = socket.ntohs(0x0800)

# create a raw socket and bind it to the public interface
s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, proto)
# s.bind(("enp9s0", 0))
s.bind(("my-tap", 0))

# Include IP headers
# s.setsockopt(socket.PF_PACKET, socket.IP_HDRINCL, 1)

# receive all packages
# s.setsockopt(socket.PACKET_OTHERHOST, 1)


while True:
   packet = s.recvfrom(2048)
   ethernet_header = packet[0][0:14]

   eth_header = struct.unpack("!6s6s2s", ethernet_header)

   print("Destination MAC:" + eth_header[0].hex() + " Source MAC:" + eth_header[1].hex() + " Type:" + eth_header[2].hex())

   ipheader = packet[0][14:34]
   ip_header = struct.unpack("!12s4s4s", ipheader)
   print("Source IP:" + socket.inet_ntoa(ip_header[1]) + " Destination IP:" + socket.inet_ntoa(ip_header[2]))



# disabled promiscuous mode
# s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)


# TAP Fun

# brctl addbr br0
# ip tuntap add name my-tap mode tap
# ip addr add 192.168.2.100 dev my-tap
# ip link set dev my-tap up
# brctl addif br0 my-tap

# interestingly, we can ping 10.0.0.1 although the interface is down?

# clean-up
# ip tuntap del my-tap mode tap
# brctl delbr br0

