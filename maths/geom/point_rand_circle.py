import numpy as np
import numpy.random as rnp
import numpy.linalg as lin
import math
import matplotlib.pyplot as plt


# we have a circle with R = 1 located at the origin and select a random point in the circle
# we have a point P at P(Px|0)
# determine the mean distance between the circle point and P

# generate random points inside the unit circle
# use rejection sampling
def rndPCircle():
    flg = False
    while(not flg):
        x = 2*rnp.random()-1
        y = 2*rnp.random()-1
        if(x**2 + y**2 < 1.0):
            flg = True
            return(x,y)

# generate random points inside the unit box
# use rejection sampling
def rndPBox():
    flg = False
    while(not flg):
        x = 2*rnp.random()-1
        y = 2*rnp.random()-1
        return(x,y)

        
N = 100000
ps = np.zeros((N,2))

for k in range(N):
    # ps[k,:] = rndPCircle()
    ps[k,:] = rndPBox()

#plt.scatter(ps[:,0], ps[:,1])
#plt.show()

Px = 2

P = np.array([Px, 0])

ds = np.zeros(N)
for k in range(N):
    ds[k] = lin.norm(ps[k,:] - P)

plt.hist(ds, 50)
plt.show()

print(np.mean(ds))
