# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 10:14:11 2023

@author: 700001473
"""

def getDigits(n):
    res = [int(d) for d in str(n)]
    return(res)


ds = getDigits(2**1000)
print(sum(ds))

