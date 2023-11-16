# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 08:45:27 2023

@author: 700001473
"""

s1 = sum([i**2 for i in range(101)])
s2 = sum(range(101))**2

print(s2 - s1)
