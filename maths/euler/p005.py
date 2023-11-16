# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 15:20:08 2023

@author: 700001473
"""

from sympy import factorint

dvsrs = {}


for i in range(2,21):
    fctrs = factorint(i)
    #print(fctrs)
    for k in fctrs:
        print(k)
        if(k in dvsrs):
            dvsrs[k] = max(dvsrs[k], fctrs[k])
        else:
            dvsrs[k] = fctrs[k]
    
prod = 1
            
for k in dvsrs:
    prod = prod * (k**dvsrs[k])

print(prod)