# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 16:38:53 2015

@author: clnovak
"""


def is_palindrom(x):
    return(str(x) == str(x)[::-1])


def revert_num(x):
    return int(str(x)[::-1])


def create_palin(x):
    num = 0
    while(not is_palindrom(x)):
        temp = revert_num(x)
        x = x + temp
        num = num + 1

    return((num, x))


print(create_palin(195))
print(create_palin(265))

print(create_palin(89))



