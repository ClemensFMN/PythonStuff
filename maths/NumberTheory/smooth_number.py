# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 13:50:44 2023

@author: 700001473
"""

import sympy.ntheory as nt


def calcBSmooth(n):
    """calculate the B-smoothness of an integer n; i.e. the largest prime factor"""
    if(n==1): return(1) # factorint returns an empty dict in case of 1 -> special handling required
    fs = nt.factorint(n) # get factors
    maxfs = max(fs.keys()) # obtain max factor
    return(maxfs)



MAX = 1000000
cnt = 0


for i in range(1, MAX+1):
    b = calcBSmooth(i)
    # print(i, b)
    if(b <= 5):
        cnt += 1

print(cnt)


