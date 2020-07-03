from collections import namedtuple


Itm = namedtuple("Itm", "name desc price")

i1 = Itm("Car", "A stupid car", 3.24)

print(i1.name)
print(Itm._fields)
print(i1._asdict())
