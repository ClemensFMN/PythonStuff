# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 12:55:01 2023

@author: 700001473
"""

def fib(max_val):
    an = 1
    anp1 = 1
    
    while(anp1 <= max_val):
        yield(anp1)
        an, anp1 = anp1, anp1 + an


fibs = list(fib(4000000))

res = [i for i in fibs if i % 2 == 0]

print(sum(res))

#while(True):
#    print(next(fibs))
    

        
    