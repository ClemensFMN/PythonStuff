from scapy import *

syn = IP(dst='google.com') / TCP(dport=80, flags='S')
syn_ack = sr1(syn) # sned out a SYN, google returns a SYN/ACK, but the kernel throws back an RST as it does not expect a SYN/ACk...
# - use iptables to block??


get_str = 'GET / HTTP/1.1\r\n'
request = IP(dst='google.com') / TCP(dport=80, sport=syn_ack[TCP].dport, seq=syn_ack[TCP].ack, ack=syn_ack[TCP].seq + 1, flags='A') / get_str

reply = sr1(request)


