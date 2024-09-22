# -*- coding: utf-8 -*-
"""
Created on Tue Dec 03 13:46:55 2013

@author: novakc
"""

import numpy as np

# weights and values
#wvec = [2, 3, 5]
#vvec = [3, 5, 7]
#W = 6

# taken from Kellerer et al, Knapsack Problems (p. 16)
wvec = [2, 3, 6, 7, 5, 9, 4]
vvec = [6, 5, 8, 9, 6, 7, 3]
W = 9

# calculate the efficiency and order wvec & vvec in decreasing values of efficiency
evec = [x[0] / x[1] for x in zip(vvec, wvec)]
ind = np.argsort(evec) # this returns the index which would sort the array
ind = ind[::-1] # we want reverse ordering -> reverse the index
wvec = np.take(wvec, ind) # rebuild wvec & vvec in decreasing order of efficiency
vvec = np.take(vvec, ind)

print()
print(wvec)
print(vvec)

n = len(wvec)

wbar = 0 # current weight
vbar = 0 # current value
xvec = np.zeros(n)


for i in range(n):
    if wbar + wvec[i] <= W:
        xvec[i] = 1
        wbar = wbar+  wvec[i]
        vbar = vbar + vvec[i]



print(xvec, vbar, wbar)
