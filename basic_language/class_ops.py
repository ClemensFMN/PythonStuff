# -*- coding: utf-8 -*-
"""
Created on Thu Mar 06 09:31:40 2014

@author: NovakC
"""

class MyC():
    def __init__(self, x):
        self._x = x

    def __add__(self, v):
        return self._x + v._x

    def __mul__(self, v):
        return self._x * v._x


a = MyC(3)
b = MyC(4)

print a + b
print a*b

