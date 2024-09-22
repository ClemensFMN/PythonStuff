# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 15:44:59 2023

@author: 700001473
"""

from sympy.ntheory import legendre_symbol


p = 11


[x**2 % p for x in range(p)]

[legendre_symbol(i, p) for i in range(p)]


