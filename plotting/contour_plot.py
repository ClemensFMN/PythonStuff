# -*- coding: utf-8 -*-
"""
Created on Wed Mar 07 07:00:03 2012

@author: NovakC
"""

import numpy as np
import matplotlib.pyplot as plt

import scipy.special as special



x = np.linspace(-1,1,50)
y = np.linspace(-1,1,50)

X,Y = np.meshgrid(x,y)

Z = 2*X**2+3*Y**2

lvls = np.linspace(0,5,11)
# lvls = np.logspace(-5,1,20)
cs = plt.contour(X,Y,Z, levels=lvls)
plt.clabel(cs, inline=1, fontsize=10)

plt.plot([0,1], [1,0], '-k')

plt.grid()
# plt.savefig("output.svg")
plt.show()
