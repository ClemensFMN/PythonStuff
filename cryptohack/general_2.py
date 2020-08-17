inp = '63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'

res = []

for i in range(int(len(inp)/2)):
    print(i)
    chunk = inp[2*i: 2*i+2]
    chunk_int = int(chunk, 16)
    chunk_char = chr(chunk_int)
    print(chunk, chunk_char)
    res.append(chunk_char)

print("".join(res))


