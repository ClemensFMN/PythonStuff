# -*- coding: utf-8 -*-
"""
Created on Mon May 23 08:16:00 2016

@author: ClNovak
"""

# the task is easy to do with a dict
# i am lazy and generate the dict based on the chars in the rows (only done 
# for the first row here)

row1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[']

# the global dic describing the string substitution
dct = {}

for i in range(len(row1)-1):
    # print(row1[i], row1[i+1])
    dct[row1[i+1]] = row1[i]
