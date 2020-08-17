import base64

inp = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'

res = []

for i in range(int(len(inp)/2)):
    print(i)
    chunk = inp[2*i: 2*i+2]
    chunk_int = int(chunk, 16)
    print(chunk, chunk_int)
    res.append(chunk_int)

print(base64.b64encode((bytearray(res))))
