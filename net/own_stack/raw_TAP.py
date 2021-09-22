# inspired by https://github.com/ccie18643/PyTCP

import os
import struct
import sys
import fcntl
import socket
from scapy.all import *


TUNSETIFF = 0x400454CA
IFF_TAP = 0x0002
IFF_NO_PI = 0x1000

# prep
# mknod /dev/net/tap c 10 200
# ip tuntap add name tap mode tap
# ip link set dev tap up
# ip route add dev tap 10.0.0.0/24
# ip address add dev tap local 10.0.0.5

# clean
# ip link del tap


# OUTLINE
# we access the TAP device via /dev/net/tap and not via socket
# via ioctl we set the relevant operating mode (TAP...)
# with an os.read we retrieve data from the TAP device
# for processing / handling the data, we use scapy

# so far, we have implemented a simple ARP answer: We check for received ARP requests for our IP and build 
# together an ARP answer


try:
	tap = os.open("/dev/net/tap", os.O_RDWR)

except FileNotFoundError:
    print("stack", "<CRIT>Unable to access '/dev/net/tap' device</>")
    sys.exit(-1)

fcntl.ioctl(tap, TUNSETIFF, struct.pack("16sH", b"tap", IFF_TAP | IFF_NO_PI))


# receive a packet
while True:
    packet = os.read(tap, 2048)

    frame = Ether(packet)
    frame.show()

    #print(frame.type)

    if(frame.type == 2054): # 2054 = 0x0806 & that's ARP. Would be good to know how we can get this out of scapy...
        print("ARP")
        if(frame[ARP].op == 1): # request
            print("   req")
            if(frame[ARP].pdst == '10.0.0.4'):
                print("        for us")
                frame.show()
                answr = Ether()/ARP()
                answr[Ether].src = '72:ee:0d:8f:1e:00' # hardcoding the MAC
                answr[Ether].dst = frame[Ether].src

                answr[ARP].hwlen = 6
                answr[ARP].plen = 4
                answr[ARP].op = 2
                answr[ARP].hwsrc = '72:ee:0d:8f:1e:00' # hardcoding the MAC
                answr[ARP].hwdst = frame[Ether].src
                answr[ARP].psrc = '10.0.0.4'
                answr[ARP].pdst = frame[ARP].psrc
                answr.show()

                snd = raw(answr)
                os.write(tap, snd)
                print("Written!")

                # sendp(answr)

    
