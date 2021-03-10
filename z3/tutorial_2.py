from z3 import *

x, y = Ints('x y')
s = Solver()
s.add(x > 0, y > 0, x + y < 3)
print(s.check())

m = s.model()
print("x = %s" % m[x])

print("traversing model...")
for d in m.decls():
    print("%s = %s" % (d.name(), m[d]))
