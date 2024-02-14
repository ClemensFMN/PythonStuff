# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 15:33:21 2023

@author: 700001473
"""

import sympy as sym

x = sym.symbols('x')

p0 = x**3 + 2*x + 1
p1 = 3*x**2 + 2

q, r = sym.div(p0, p1)

sols = sym.solve(x**3 + 2*x + 1, x)

[sym.N(sol) for sol in sols]


# import matplotlib.pyplot as plt
# import numpy as np

# x = np.linspace(-2,2,num=100)

# y = x**3 + 2*x + 1

# plt.plot(x,y)
# plt.axes(True)





