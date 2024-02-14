# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 13:41:56 2024

@author: 700001473
"""

from sympy import series, cos, ln, binomial
from sympy.abc import a, n, x

# s = series(cos(x), x)

# s = series(ln(x), x, 1)

s = series((1+x)**a, x, 0, 5)


a = 5

for n in range(0, 10):
    term = binomial(-a+n-1, n)*(-x)**n
    print(term)

    term = binomial(a, n)*x**n
    print(term)




# series(ln(1+x)/x, x, 0, n=10)
