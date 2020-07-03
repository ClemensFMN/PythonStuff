# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 15:36:17 2015

@author: ClNovak
"""

def funny_counter(max_val):
    print("starting", max_val)
    i = 0    
    while i < max_val:
        yield i
        i = i + 1
    #raise StopIteration()

for i in funny_counter(5):
    print(i)