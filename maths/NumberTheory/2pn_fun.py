# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 11:05:12 2023

@author: 700001473
"""

import numpy as np
import matplotlib.pyplot as plt

N = range(2, 100)


len_2on = []
sum_2pn = []

for n in N:
    val = 2**n
    s = str(val)
    
    len_2on.append(len(s))
    
    digits = [int(c) for c in s]
    #print(digits)
    sum_2pn.append(sum(digits))


len_2pn_an = N * np.log10(2)
sum_2pn_an = N * np.log10(2) * 4.5


if(False):
    plt.plot(N, len_2on, '-rx', N, len_2pn_an, '-g')
    plt.plot(N, sum_2pn, '-rx', N, sum_2pn_an, '-g')

