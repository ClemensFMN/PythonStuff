# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 11:29:41 2023

@author: 700001473
"""

# based on https://stackoverflow.com/questions/40190849/efficient-finding-primitive-roots-modulo-n-using-python

from math import gcd

def primRoots(modulo):
    coprime_set = {num for num in range(1, modulo) if gcd(num, modulo) == 1}
    return [g for g in range(1, modulo) if coprime_set == {pow(g, powers, modulo)
            for powers in range(1, modulo)}]

# the number we are working on
p = 13

# first we calculate the orders of all numbers 1...p-1
from sympy.ntheory import n_order, totient
orders = [(k, n_order(k, p)) for k in range(1,p-1)] # returning (number, order)
print(orders)

# using the function above, obtain the primitive roots of p
# alternative would be to filter previous order result for orders == p-1
# [n for (n,o) in orders if o == p-1]
primitive_roots = primRoots(p)
print(primitive_roots)

# n has totient(totient(p)) primitive roots



