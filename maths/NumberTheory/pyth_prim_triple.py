import math
import matplotlib.pyplot as plt

N = 50

pointsx = []
pointsy = []

for t in range(1, N):
    for s in range(t, N):
        if(math.gcd(s,t) == 1):
            if(s % 2 != t % 2):
                # print(s,t)
                x = 2*s*t
                y = s**2 - t**2
                z = s**2 + t**2
                if(z < N**2):
                    print(x,y,z)
                    pointsx.append(x)
                    pointsy.append(y)
            
print(len(pointsx))


plt.scatter(pointsx, pointsy, s=1, c='b')
plt.scatter(pointsy, pointsx, s=1, c='b')
plt.grid()
plt.show()
