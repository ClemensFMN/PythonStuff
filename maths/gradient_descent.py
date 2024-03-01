# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 10:49:58 2023

@author: 700001473
"""

from sympy.abc import x, y
from sympy import plot, diff, solve


# we want to find the minima of f(x)
f = x**4 - 3*x**2

df = diff(f,x)
res = solve(df, x)
resn = [x.evalf() for x in res]
print(resn)


gamma = 0.1

delta = 1.0

xn = 0.5
xns = [xn]

for it in range(100):
    
    xnp1 = xn - gamma*df.subs(x, xn)
    xns.append(xnp1)
    delta = abs(xn - xnp1)
    
    print(xnp1, delta)
    
    if(delta < 1e-5):
        break
    xn = xnp1
    

print(it, xn)

# plot(f,(x,-2,2))




