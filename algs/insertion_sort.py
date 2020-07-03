# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 10:27:55 2015

@author: ClNovak
"""

def sort_v1(lst):
    for j in range(1, len(lst)):
        # loop invariant -> at the beginning of the loop, the elements
        # of lst[0:j-1] contain the elements of A[0:j-1] but in sorted order
        print(j, lst[0:j])
        # select "key"; i.e. element to insert
        key = lst[j]
        #print("pos, key ->", j, key)
        i = j - 1
        # here we combine two operations:
        # (i) search for the right insertion position
        # (ii) shift stuff to the right
        # in the version below, these are two separate loops
        while (i>=0 and lst[i] > key):
            lst[i+1] = lst[i]
            i = i - 1
        #print("shifted", lst)
        # insert key
        lst[i+1] = key
        #print("inserted", lst)
    return(lst)

def sort_v2(lst):
    for j in range(1, len(lst)):
        # select "key"; i.e. element to insert
        key = lst[j]
        print(j, key)
        
        # default value of the insert position is the current position
        insert_pos = j

        # now try to find the new insert position        
        for i in range(0, j):
            if(lst[i] > key):
                # i is the new placement position -> we are finished
                insert_pos = i
                break                
        # if the if condition is never true, we have as fallback insert_pos the current one
        print("...", insert_pos)

        # now shft stuff to the right
        for k in range(j, insert_pos, -1):
                lst[k] = lst[k-1]
        print("moved", lst)
        lst[insert_pos] = key
        print("inserted", lst)


# A = [5,2,4,6,1,3]

A = [34, 78, 2, 6 , 1, 9, 4]
print(A)

#print(sort_v1(A))

print(sort_v2(A))
