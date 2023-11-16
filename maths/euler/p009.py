# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 09:29:23 2023

@author: 700001473
"""

for a in range(1, 1001):
    for b in range(1, 1001):
        c = 1000 - a - b
        if(c > 0 and a**2 + b**2 == c**2):
            print(a,b,c, a*b*c)