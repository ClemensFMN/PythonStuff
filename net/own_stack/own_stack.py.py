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

# prep moved to setup.sh

# clean
# ip link del tap


# OUTLINE
# we access the TAP device via /dev/net/tap and not via socket
# via ioctl we set the relevant operating mode (TAP...)
# with an os.read we retrieve data from the TAP device
# for processing / handling the data, we use scapy
# Implemented:
# answering ARP requests and storing answer in ARP cache
# detect incoming ICMP request
# build up ICMP packet but without payload 




STACK_MAC = '72:ee:0d:8f:1e:00'
STACK_IP = '10.0.0.4'


ARP_table = {}



def arp_handler(frame):
    if(frame[ARP].op == 1): # request
        print("ARP req")
        if(frame[ARP].pdst == STACK_IP):
            print("        for us")
            # frame.show()
            answr = Ether()/ARP()
            answr[Ether].src = STACK_MAC
            answr[Ether].dst = frame[Ether].src

            answr[ARP].hwlen = 6
            answr[ARP].plen = 4
            answr[ARP].op = 2
            answr[ARP].hwsrc = STACK_MAC
            answr[ARP].hwdst = frame[Ether].src
            answr[ARP].psrc = STACK_IP
            answr[ARP].pdst = frame[ARP].psrc
            # answr.show()

            ARP_table[frame[ARP].psrc] = frame[Ether].src
            print(ARP_table)

            snd = raw(answr)
            os.write(tap, snd)
            print("Written!")


def ip_handler(frame):
    if(frame[IP].version == 4):
        if(frame[IP].proto == 1):
            if(frame[ICMP].type == 8):
                print("ICMP echo request")
                answr = Ether()/IP()/ICMP()
                answr[Ether].src = STACK_MAC
                answr[Ether].dst = ARP_table[frame[IP].src] # TODO: Add error checking: send ARP requets when we don't know the SRC MAC?

                answr[IP].src = STACK_IP
                answr[IP].dst = frame[IP].src

                answr[ICMP].type = 0
                # TODO: Add payload

                answr.show()



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
    # frame.show()

    if(frame.type == ETH_P_ARP):
        print("ARP")
        arp_handler(frame)
    elif(frame.type == ETH_P_IP):
        print("IP")
        ip_handler(frame)
    else:
        print("unknown type")




    
