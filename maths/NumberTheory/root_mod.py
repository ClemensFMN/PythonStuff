# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 13:20:24 2023

@author: 700001473
"""

from sympy.ntheory import legendre_symbol
from sympy.ntheory import sqrt_mod


print(legendre_symbol(24, 29))
print(sqrt_mod(24, 29, all_roots=(True))) # yields 13, 16

print(13**2 % 29)
print(16**2 % 29)
