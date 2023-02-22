# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 12:08:54 2023

@author: 700001473
"""

from sympy.ntheory import *

# 5**x \equiv 2 \mod 5 -> x = 4
# print(discrete_log(p, 2, 5)) # yields 4

# solving our x^2 \equiv 3 \mod 13 problem
# primitive roots of 13 are: 2, 6, 7, 11

p = 13
# all 4 indices are even: d = 2 | ind -> it does not matter which primitive root are using, we will always get the same solutions...
print(discrete_log(13, 3, 2))
print(discrete_log(13, 3, 6))
print(discrete_log(13, 3, 7))
print(discrete_log(13, 3, 11))

# x^2 \equiv 3 \mod 13 -> 2 solutions
print(sqrt_mod(3, 13, all_roots=(True)))
# check via Euler's criteria
# a^(p-1)/2 \equiv 1 \mod p
print("Euler: ", 3**((p-1)/2) % p)

# x^2 \equiv 5 \mod 13 -> no solutions
print(sqrt_mod(5, 13, all_roots=(True)))
# check via Euler's criteria
# a^(p-1)/2 \equiv 1 \mod p
print("Euler: ", 5**((p-1)/2) % p)
