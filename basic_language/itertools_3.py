# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 21:04:22 2015

@author: ClNovak
"""

# itertools - generators

import itertools as it

ls = ['a', 'b', 'c', 'd']

ls1 = zip(ls, it.count(10))

# returns iterators -> can be consumed only once
# either this way
#for elem in ls1:
#    print(elem)

# or that way
print(list(ls1))

print(list(it.accumulate([4,2,3], lambda x,y: x*y)))

print("Combinations")
# 4 over 2 = 4x3/2 elements
print(list(it.combinations(ls, 2)))

print("Permutations")
# 4x3 elements
print(list(it.permutations(ls, 2)))

print("Combinations with replacement")
# i think it's 5 over 2 = 5x4/2 = 10 elements (combintions of multisets)
print(list(it.combinations_with_replacement(ls, 2)))

print("Product")
# 4**2 elements
print(list(it.product(ls, ls)))

#powerset = [it.combinations(ls,s) for s in range(len(ls))]
##powerset = it.chain.from_iterable(powerset)
##print(list(powerset))
#
#powerset = [list(x) for x in powerset]
#print(powerset)

lst = range(0,4)

res = it.product(lst, lst)
# filter everything for which the second element is larger than the first
res = it.filterfalse(lambda e: e[0] < e[1], res)

print(list(res))

print()

res = it.product(lst, lst)
# filter everything non-distinct
res = it.filterfalse(lambda e: e[0] == e[1], res)

print(list(res))

