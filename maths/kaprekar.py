# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 11:37:03 2024

@author: 700001473
"""

# https://en.wikipedia.org/wiki/6174

def kaprekar(x):
    digits = [int(d) for d in str(x)]
    digits_asc = sorted(digits)
    x_asc = digits_asc[0] + digits_asc[1]*10 + digits_asc[2]*100 + digits_asc[3]*1000
    digits_des = sorted(digits, reverse=True)
    x_des = digits_des[0] + digits_des[1]*10 + digits_des[2]*100 + digits_des[3]*1000
    diff = abs(x_asc - x_des)
    return(diff)


start = 1459

# res = kaprekar(start)

for _ in range(10):
    print(start)
    start = kaprekar(start)
