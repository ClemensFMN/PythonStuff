# -*- coding: utf-8 -*-
"""
Created on Tue Dec 03 13:46:55 2013

@author: novakc
"""

import numpy as np


wvec = [2, 3, 5]
vvec = [3, 5, 1]


W = 5

n = len(wvec)

# the total value vector
m = np.zeros((n, W+1))
content = {}


# special treatment for the 0-th row
for j in range(W+1):
    
    if wvec[0] > j:
        # the 0-th item does not yet fit into the bag
        # -> zero total value
        m[0, j] = 0
        # and no item
        content[(0, j)] = []

    else:
        # the 0-th item fits into the bag -> add it        
        # set total value accordingly        
        m[0, j] = vvec[0]
        # and add the 0-th item
        content[(0, j)] = [0]


for i in range(1, n):

    for j in range(W+1):

        if j >= wvec[i]:
            # the i-th element would fit in -> there are two options
            # option 1: keep the previous content
            cand1 = m[i-1, j]
            # option #2: add this new item
            cand2 = m[i-1, j-wvec[i]] + vvec[i]

            # do what yields a higher total value
            m[i, j] = max(cand1, cand2)
            
            # and update the bag content accordingly
            if(cand1 > cand2):
                # option 1: keep previous content
                temp = content[(i-1, j)]
                content[(i, j)] = list(temp)
            else:
                # options 2: add new item
                temp = content[(i-1, j-wvec[i])]
                content[(i, j)] = list(temp)
                content[(i, j)].append(i)

        else:
            # i-th element does not fit -> only option 1: keep 
            # previous content
            m[i, j] = m[i-1, j]
            temp = content[(i-1, j)]
            content[(i, j)] = list(temp)

print(m)
print(content)

