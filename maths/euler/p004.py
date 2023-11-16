# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 13:30:00 2023

@author: 700001473
"""

def isPalindrome(n):
    dgts = [int(i) for i in str(n)]
    #print(dgts)
    rev = dgts[::-1]
    #print(rev)
    return(dgts == rev)

mx = 0

for i in range(1, 1000):
    for j in range(1,1000):
        prod = i * j
        if(isPalindrome(prod) and prod > mx):
            mx = prod
