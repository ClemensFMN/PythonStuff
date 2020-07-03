import re

s = '12.456'

b = re.match(r"(\d+)\.(\d+)", s)

c = b.groups()

print(c)

print(c[0], c[1])


#================================================

s = '12.456 67.897 45'

b = re.findall(r"(\d+)\.*(\d*)", s)

print(b)


#================================================

s = '12.456 67.897 45'

b = re.finditer(r"(\d+)\.*(\d*)", s)

for element in b:
    print(element.start(), element.group())


