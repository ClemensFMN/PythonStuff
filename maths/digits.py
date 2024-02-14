# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 08:39:40 2024

@author: 700001473
"""

"""
Based on a dicsussion in math-fun mailing list: 1234 - 5 + 6 + 789 = 2024

So let's split the numbers 1 - 9 into num_groups groups (there are mostly several options to do this; 12 34 56 789)
and combine them all possible combinations of +- and see which numbers come out; eg

1234 + 5 + 6 + 789
1234 + 5 + 6 - 789
1234 + 5 - 6 + 789
...
    
"""


from itertools import *
from more_itertools import *
import operator
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter


def iter2num(it):
    """Convert a list of digits into a number
    
    Examples:
        iter2num([2,3,4]) -> 234
        iter2num([5]) -> 5
        iter2num([1,0,3,4]) -> 1034
    """
    res  = 0
    for i in range(0, len(it)):
        res += it[len(it)-1 - i]*10**i
    return(res)




def applyop(nums, op):
    """apply the sequence of operations to the numbers in the list
    
        Examples:
            res = applyop([3,4,5,6], [operator.add, operator.sub, operator.add]) -> 3+4-5+6 = 8
    """
    res = nums[0]
    for ind in range(len(op)):
        o = op[ind]
        num = nums[ind+1]
        res = o(res, num)
        # print(ind, o, num, res)
    return(res)



def allops(nums):
    """takes a list of numbers and creates all values obtained by performing all ops sequences
    
        Examples:
            res = allops([1,2,3]) -> [6, 0, 2, -4]
            1+2+3 = 6
            1+2-3 = 0
            1-2+3 = 2
            1-2-3 = -4
    """
    ops = product([operator.add, operator.sub],repeat=len(nums)-1)
    ret = []
    for o in ops:
        # print(o)
        res = applyop(nums, o)
        #print(res)
        ret.append(res)
    return(ret)
        



nums = [1,2,3,4,5,6,7,8,9]



num_groups = 3
vals = []
res = partitions(nums)

for elem in res:
    # print(elem, len(elem))
    if(len(elem) == num_groups):
       # print(elem)
        num = np.zeros(num_groups)
        for i in range(num_groups):
            num[i] = iter2num(elem[i])
        #print(num)
        res = allops(num)
        # print(num, res)
        # that's super-ugly: iterate across all result arrays & append the elements one by one 
        for r in res:
            vals.append(r)


# analysis / visualisation
cnt = Counter(vals)
min(vals)
max(vals)

density = len(vals) / (max(vals) - min(vals))

years = [x for x in vals if x in range(1900,2100)]
print(years)

