# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 21:17:53 2012

@author: cnovak
"""

import matplotlib.pyplot as plt
import numpy as np

l1 = [(x,y) for x in range(5) for y in range(5) if x <= y]

print l1



x = []
y = []

for item in l1:
    x.append(item[0])
    y.append(item[1])


plt.plot(x,y,'rx', markersize=10)

#plt.savefig("test.png")
plt.show()
