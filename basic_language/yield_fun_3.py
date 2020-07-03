# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 16:16:14 2012

@author: novakc
"""


# simple generator example
# a normal function yields some values
# the function returns a generator object and can be used in a for loop 
# as below
# every yield causes the function to suspend and return the yielded value
# to the for loop
def myGenerator():
    print("1st value")
    yield(10)
    print("2nd value")
    yield(20)
    print("3rd value")
    yield(30)

for i in myGenerator():
    print(i)

print("******************")

# the generator can potentially return endless sequences of numbers
# in this case, the for loop needs to terminate "early"
def endlessNumbers():
    n = 0
    while(True):
        yield(n)
        n = n + 1

for (num, val) in zip(range(10), endlessNumbers()):
    print(num, val)

print("******************")

# the function returning the generator is a normal function and can 
# take parameters. These can affect the yielded values
def parameterizedNumbers(x):
    while(True):
        yield(x)
        x = x + 1

for (num, val) in zip(range(10), parameterizedNumbers(10)):
    print(num, val)




