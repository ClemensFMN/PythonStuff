# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 14:34:23 2013

@author: cnovak
"""

import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt

# lst = [11, 1, 2, 3, 4, 5]


Nvec = [5, 10, 20, 50, 100, 200]
runs = 50

count_vec = np.zeros((runs, len(Nvec)))



for Nind, N in enumerate(Nvec):
    
    for runind in range(runs):
    
        lst = rand.uniform(size=N)
    
        # print lst
    
        swapped = False
    
        count = 0
    
        while True:
    
            #print lst
    
            for ind in range(0, len(lst)-1):
                # swap elements which are in wrong order
                if lst[ind+1] < lst[ind]:
                    temp = lst[ind+1]
                    lst[ind+1] = lst[ind]
                    lst[ind] = temp
                    # and store that we swapped
                    swapped = True
                    count = count + 1
        
            # no more swaps in the last pass -> finish
            if swapped == False:
                break
        
            swapped = False

        count_vec[runind, Nind] = count

#print count_vec
counts = np.average(count_vec, axis=0)

plt.loglog(Nvec, counts)
plt.grid()
plt.show()

