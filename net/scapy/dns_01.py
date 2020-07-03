# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 10:49:46 2016

@author: clnovak
"""

from scapy.all import *

dns_only = DNS(rd=1,qd=DNSQR(qname="www.thepacketgeek.com"))
dns_packet = IP(dst="8.8.8.8")/UDP(dport=53)/dns_only
dns_packet.show()

hexdump(dns_only)
hexdump(dns_packet)
