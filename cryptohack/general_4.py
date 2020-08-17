import Crypto.Util.number as num

msg = 11515195063862318899931685488813747395775516287289682636499965282714637259206269 # 310400273487
hx = hex(msg)

hx = hx[2:]

chunks = []

for i in range(int(len(hx)/2)):
    tmp = hx[2*i:2*i+2]
    chunks.append(chr(int(tmp, 16)))

res = "".join(chunks)
print(res)
