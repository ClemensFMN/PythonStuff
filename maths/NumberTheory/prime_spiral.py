# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 10:56:31 2023

@author: 700001473
"""

import numpy as np
import matplotlib.pyplot as plt
import sympy.ntheory as nth



#r = np.arange(0, 2, 0.01)
#theta = 2 * np.pi * r

N = 2000

s = nth.Sieve()
s.extend_to_no(N)

r = s._list
theta = r


fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
# ax.plot(theta, r, 'rx')
ax.scatter(theta, r, s=1, c='b')
#ax.set_rmax(2)
#ax.set_rticks([0.5, 1, 1.5, 2])  # Less radial ticks
#ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
ax.grid(True)

ax.set_title("A line plot on a polar axis", va='bottom')
plt.show()

