# using list comprehension

xrd = [13 ^ ord(x) for x in 'label']

s = [chr(x) for x in xrd]
res = "".join(s)

print(res)
