# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 15:29:43 2012

@author: novakc
"""

def duplicate(s):
    return s + s

def unity(s):
    return s

def process(f, s):
    return f(s)


text = "Susi loves you"

print(text, process(unity, text))

print(text, process(duplicate, text))



