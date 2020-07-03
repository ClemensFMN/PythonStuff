# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 16:16:14 2012

@author: novakc
"""

def funny_counter(max_val):
    """return a generator
    input: max_val
    output: generator, to be used as:
        for i in funny_counter(10)
            print i
    """
    print("starting", max_val)
    i = 0
    while i < max_val:
        yield i
        i = i + 1

for i in funny_counter(5):
    print(i)



