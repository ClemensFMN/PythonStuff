# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 10:52:31 2016

@author: clnovak
"""

from scapy.all import *

ip_packet = IP(dst="8.8.8.8")/ICMP()

ip_packet.show()


# requires root (execute file via %run ip_01.py on console)
rx = sr(ip_packet)


# continue as follows
ans,unans=rx

ans[0][1].show()

