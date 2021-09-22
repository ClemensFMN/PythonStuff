# -*- coding: utf-8 -*-


from scapy.all import *

dns_only = DNS(rd=1,qd=DNSQR(qname="www.thepacketgeek.com"))

dns_packet = IP(dst="172.16.1.102")/UDP()/dns_only
dns_packet.show()

hexdump(dns_packet)


reply = sr1(dns_packet)
reply.show()
