# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 12:14:55 2015

@author: clnovak
"""

import random

# recursive variant of quicksort
def qsort_v1(lst):
    # called with a list having one element -> we are done
    if(len(lst) <= 1):
        return(lst)
    else:
        # find pivot element (here the last element of the list)
        pivot = lst[-1]
        # the problem here is that duplicates of the pivot element appear 
        # in neither left / right list and therefore "fall out"
        # split list into stuff smaller than pivot
        #left = [i for i in lst if i < pivot]
        # and larger than pivot
        #right = [i for i in lst if i > pivot]

        # split list
        left = [i for i in lst[0:len(lst)-1] if i < pivot]
        right = [i for i in lst[0:len(lst)-1] if i >= pivot]
        # qsort the left and right parts
        l1 = qsort_v1(left)
        r1 = qsort_v1(right)


        # and build up the result
        return(l1 + [pivot] + r1)

# partition lst between p and r
# pivot = lst[r]
# all elements < pivot are in lst at indices < i
# all elements > pivot are in lst at indices > i
# the pivot is at index i
def partition(lst, p, r):
    pivot = lst[r]
    i = p - 1
    for j in range(p, r):
        if(lst[j] < pivot):
            i = i + 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i+1], lst[r] = lst[r], lst[i+1]
    return(i+1)

# recursive quicksort using the partition function
# this one works with duplicate elements
def qsort_v2(lst, p, r):
    if(p<r):
        q = partition(lst, p, r)
        qsort_v2(lst, p, q-1)
        qsort_v2(lst, q+1, r)


# A = [34, 78, 2, 6, 1, 9, 4]
# A = [34, 34, 78, 31]
A = [34, 34, 78, 12, 26, 31, 9, 4, 10]

#random.shuffle(A)
print(A)

# A = random.sample(range(100), 10)

res = qsort_v1(A)
print(res)


#qsort_v2(A, 0, len(A)-1)
#print(A)


#print(A)
#res = partition(A, 0, len(A)-1)
#print(res, A)
#
## check invariants
#
#check = True
#for i in range(0, res):
#    if(A[i] > A[res]):
#        check = False
#
#print(check)
#
#check = True
#for i in range(res, len(A)-1):
#    if(A[i] < A[res]):
#        check = False
#
#print(check)
#
