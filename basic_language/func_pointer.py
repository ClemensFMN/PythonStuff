# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 08:18:02 2014

@author: novakc
"""

def func1(x):
    return 2*x

def func2(x):
    return 3*x



class c1:
    def __init__(self, x):
        self.x = x

    def printMe(self):
        print self.x


class c2:
    def __init__(self, x):
        self.x = x

    def printMe(self):
        print 2*self.x


func_pointer = func1
print func_pointer(2)


func_pointer = func2
print func_pointer(3)


print "***************************"

class_map ={"class1": c1, "class2": c2}

for key in class_map.keys():
    class_pointer = class_map[key]
    c = class_pointer(3)
    print key
    c.printMe()

