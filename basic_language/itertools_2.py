# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 13:01:18 2015

@author: ClNovak
"""

# itertools - iterators

import itertools as it

lst = [1,2,2,5,4,0,1,6,7,9]

# create a new group upon change of the predicate
res = it.groupby(lst, lambda x: x%2==0)

for k,g in res:
    print(k, list(g))


print("")

# remove everything for which the predicate is true
res = it.filterfalse(lambda x: x%2==0, lst)

print(list(res))

