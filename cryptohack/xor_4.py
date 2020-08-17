import more_itertools as mi

s = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'

chunks = mi.windowed(s, n=2, step=2)

chunks_comb = [e[0] + e[1] for e in chunks]
chunks_num = [int(e, 16) for e in chunks_comb]


key = []
for (ind, val) in enumerate('crypto{'):
    key.append(ord(val) ^ chunks_num[ind])

key_s = "".join([chr(e) for e in key])
print(key_s)

# ok, now we can guess that the key shold be
final_key = key + [ord('y')]



rep_key = final_key * (1 + int(len(chunks_num) / len(final_key)))
rep_key = rep_key[:len(chunks_num)]

res = []

for i in range(len(chunks_num)):
    res.append(rep_key[i] ^ chunks_num[i])

res_final = "".join([chr(e) for e in res])
print(res_final)






# obtaining the key called key
# let's assume the output has the form crypto{FLAG}
# this means that chunks_num[0] ^ key = 'c'
# xor'ing both sides with chunks_num[0] yields: key = 'c' ^ chunks_num[0]
#key = ord('c') ^ chunks_num[0]

#chunks_dec = [key ^ e for e in chunks_num]

#chunks_dec_chr = [chr(e) for e in chunks_dec]

#res = "".join(chunks_dec_chr)
#print(res)
