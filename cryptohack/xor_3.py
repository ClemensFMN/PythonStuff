import more_itertools as mi

s = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'

chunks = mi.windowed(s, n=2, step=2)

chunks_comb = [e[0] + e[1] for e in chunks]
chunks_num = [int(e, 16) for e in chunks_comb]

# obtaining the key called key
# let's assume the output has the form crypto{FLAG}
# this means that chunks_num[0] ^ key = 'c'
# xor'ing both sides with chunks_num[0] yields: key = 'c' ^ chunks_num[0]
key = ord('c') ^ chunks_num[0]

chunks_dec = [key ^ e for e in chunks_num]

chunks_dec_chr = [chr(e) for e in chunks_dec]

res = "".join(chunks_dec_chr)
print(res)

# for fun and completeness, we can use the remaining known entries in the flag to obtain /check the key (this is interesting for the next challenge)
# print(ord('r') ^ chunks_num[1])
for (ind, val) in enumerate('crypto'):
    print(ord(val) ^ chunks_num[ind])


