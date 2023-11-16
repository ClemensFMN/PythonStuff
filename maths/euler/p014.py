# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 13:45:19 2023

@author: 700001473
"""

def collatz(n):
    cnt = 1
    nxtVal = n
    while(nxtVal != 1):
        if(nxtVal %  2 == 0):
            nxtVal = int(nxtVal / 2)
        else:
            nxtVal = 3*nxtVal + 1
        #print(nxtVal)
        cnt += 1
    return(cnt)

collatz(13) # returns 10

# now let's improvie performance by using a cache
collCache = {}

def collatz_v2(n):
    cnt = 1
    nxtVal = n
    while(nxtVal != 1):
        # for every new input value we look in the cache first
        if nxtVal in collCache:
            #print("cache hit", nxtVal)
            collCache[n] = collCache[nxtVal] + cnt - 1
            return(collCache[n])
        if(nxtVal %  2 == 0):
            nxtVal = int(nxtVal / 2)
        else:
            nxtVal = 3*nxtVal + 1
        #print(nxtVal)
        cnt += 1
    collCache[n] = cnt
    return(cnt)



# below code gives 525 as longest sequence but according to Project Euler, this is wrong?!
maxLen = 1
maxStart = 1

for i in range(2, 1000001):
    ln = collatz_v2(i)
    if(ln > maxLen):
        maxLen = ln
        maxStart = i
    #print(i, " => ", ln)

print(maxStart, maxLen)



