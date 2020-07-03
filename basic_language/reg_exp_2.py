# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 11:37:30 2012

@author: novakc
"""

import re

"""
s contains a chemical formula, weights contains the weights of the molecules.
The formula is parsed & the number of every molecule is multiplied with its weight,
giving the total weight. 
"""

s = 'H2COH2N'

weights = {'H': 2, 'COH' : 4, 'N' : 1}

s_parsed = re.findall(r"([A-Z]+)(\d*)", s)

print(s_parsed)

weight = 0

for item in s_parsed:
    print(item)
    if(item[1] != ''):
        val = int(item[1]) * weights[item[0]]
    else:
        val = weights[item[0]]

    weight += val


print("Totoal Weight:", weight)
