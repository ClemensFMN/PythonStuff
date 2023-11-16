# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 13:17:19 2023

@author: 700001473
"""

maxV = 1000

mul3 = [3*i for i in range(1,maxV) if 3*i < maxV]
mul5 = [5*i for i in range(1,maxV) if 5*i < maxV]

res = set(mul3).union(set(mul5))
print(sum(res))


