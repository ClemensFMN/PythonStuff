# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 13:37:21 2023

@author: 700001473
"""

from sympy.ntheory import quadratic_residues
import numpy as np
import matplotlib.pyplot as plt

N = 1000

num_q_res = np.zeros(N)


for i in range(1, N):
    num_q_res[i] = len(quadratic_residues(i))

plt.plot(num_q_res,'rx')
plt.grid(True)