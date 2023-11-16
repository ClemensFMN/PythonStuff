# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 09:35:18 2023

@author: 700001473
"""

import math
import matplotlib.pyplot as plt


def is_square(integer):
    root = math.sqrt(integer)
    return integer == int(root + 0.5) ** 2

N = 2500

pointsx = []
pointsy = []

for x in range(1, N):
    for y in range(1, N):
        zsqu = x**2 + y**2
        if(is_square(zsqu)):
            print(x,y,math.sqrt(zsqu))
            pointsx.append(x)
            pointsy.append(y)
            
# print(len(pointsx))


plt.scatter(pointsx, pointsy, s=1, c='b')
plt.grid()
plt.show()
