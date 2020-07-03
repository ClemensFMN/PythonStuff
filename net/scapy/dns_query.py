

request = IP(dst='172.16.1.102')/UDP()/DNS(rd=0, qd=DNSQR(qname='www.slashdot.org'))

reply = sr1(request)
