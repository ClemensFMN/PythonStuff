#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 11:51:50 2019

@author: clnovak
"""
import array

lst1 = tuple(n for n in range(1,10) if n % 2 == 0)
print(lst1) # generate a tuple which is immutable


lst2 = array.array('I', (n for n in range(1,10) if n % 2 == 0))
print(lst2)


lst3 = list(filter(lambda x: x % 2 == 0, range(1,10)))
print(lst3)

lst4 = tuple((n, n**2) for n in range(5))
print(lst4)

for (x,y) in lst4:
    print(x,y)  # tuple unpacking


