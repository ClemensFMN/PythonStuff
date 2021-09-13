# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 10:52:54 2012

@author: cnovak
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.misc as misc
import scipy.special as special


def f1(x):
    res = x**2
    return(res)

def f2(x, alpha):
    res1 = np.sin(alpha*x)
    res2 = np.cos(alpha*x)
    return(res1, res2)




#x = np.linspace(0, 1, 100)
#plt.plot(x, f1(x), '-r', label='f1(x)')
#plt.title('One-function Plot')




x = np.linspace(-np.pi, np.pi, 100)
y1, y2 = f2(x, 1.3)
plt.plot(x, y1, '-g', label='f1(x)')
plt.plot(x, y2, '-r', label='f2(x)')
plt.title('Two-function Plot')

plt.legend()
plt.grid()
# plt.savefig("output.png")
plt.show()
