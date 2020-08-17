import more_itertools as mi



# we know the follogin data
KEY1 = int('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313', 16)
KEY2xorKEY1 = int('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e', 16)
KEY2xorKEY3 = int('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1', 16)
FLAGxorKEY1xorKEY3xorKEY2 = int('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf', 16)

# this calcs the xor of all three keys
temp1 = KEY1 ^ KEY2xorKEY3

# since A xor A = 0, this xor operation removes all 3 keys & returns the flag...
flg = FLAGxorKEY1xorKEY3xorKEY2 ^ temp1

hxflag = hex(flg)

hxflag = hxflag[2:]

# option 1
chunks = []

for i in range(int(len(hxflag)/2)):
    tmp = hxflag[2*i:2*i+2]
    chunks.append(chr(int(tmp, 16)))

res = "".join(chunks)
print(res)

# option 2
chunks = mi.windowed(hxflag, n=2, step=2)
chunks_comb = [e[0] + e[1] for e in chunks]
chunks_char = [chr(int(e, 16)) for e in chunks_comb]
res = "".join(chunks_char)
print(res)
