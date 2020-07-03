# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 17:31:30 2016

@author: clnovak
"""

def func(x):
    return(x+1)


#def decorator(x):
#    return(x)


def decorator(F):
    def wrapper(x):
        val = F(x)
        print(x, val)
        return(val)
    return wrapper


@decorator
def func2(x):
    return(x+2)



print(func(4))

val = func2(10)
print(val)

