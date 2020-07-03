# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 16:10:45 2012

@author: novakc
"""

a = [1, 3, 4, 7, 8]

b = (2*x for x in a)

c = (2*x for x in a if x%2==0)

d = ((x,2*x) for x in a)

for i in b:
    print i

print ''

for i in c:
    print i

print ''

for i in d:
    print i , "   " , i[0] , "->" , i[1]
