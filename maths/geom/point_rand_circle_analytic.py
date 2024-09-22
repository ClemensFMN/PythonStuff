import scipy.integrate as int
import numpy as np

# numerical solution to the problem of calculating the expected distance between a fixed point and a
# random point inside the unit box

def d(x,y):
    return 1/4*np.sqrt((xp - x)**2 + y**2)

xp = 2.0

res = int.dblquad(d, -1, 1, -1, 1)
print(res)

