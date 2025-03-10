# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 12:45:58 2025

@author: x372924
"""

import numpy as np
import scipy as sci
import matplotlib.pyplot as plt


# we consider the following geometrical problem
# a rectangle of with 1 and height 5 needs to be crossed
# from the lower right to the upper left corner
# we can go up & diagonal: First we go x units up, then diagonal
# to the left upper corner.
# The total length L = x + \sqrt{(5-x)^2 + 1^2}
# and we calculate and plot it below
# 
# x───────────────────────────────  
#  xxx                             │
#    xxx                           │
#       xxx                        │
#          xx                      │
#            xxx                   │
#               xxx                │
#                 xxxx             │
#                     xxx          │
#                        xx        │
#                         xxxx     │
#                             xxxx │
#                                xxx        x
#                                 x│
#                                 x│
#                                 x│
#                                 x│
#                                 x│
#                                 x│
#                                 xx


x = np.linspace(0,5)

L = x + np.sqrt((5-x)**2 + 1)

# at the extreme point x = 0, we have L = sqrt{5^2 + 1} = \sqrt{26}
# the other extreme point is x = 5: we go all the way up and then left.
# Therefore L = 5 + 1 = 6
# Interestingly, the shortest way is when we move diagonally as early as possible


plt.plot(x, L)
plt.grid(True)

# TODO (idea): Consider the ration between shortest & longest path as function
# of width & height of the rectangle (I assume only the ratio of the 2 is important)