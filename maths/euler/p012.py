# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 10:26:25 2023

@author: 700001473
"""

import math


def getDivisors(n):
    # get the divisors of a number - probably rather inefficient :-(
    divs = [1]
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            divs.extend([i,int(n/i)])
    divs.extend([n])
    return sorted(list(set(divs)))

def triangleNumber():
    # setup a generator for triangle numbers
    i = 1
    ti = i
    while(True):
        yield(ti)
        i = i + 1
        ti = ti + i
        
t = triangleNumber()

while(True):
    tn = next(t)
    cnt = len(getDivisors(tn))
    if(cnt > 500):
        break




