# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 11:28:29 2016

@author: clnovak
"""

import re

def print_result(b):
    for element in b:
        print(element.start(), element.end(), element.group())

# optional elements
s = 'Jul July'
b = re.finditer(r"July?", s)

print_result(b)

print("**********")

s = 'J Jul July'
b = re.finditer(r"J(uly)?", s)

print_result(b)





