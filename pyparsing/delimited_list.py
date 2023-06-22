# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 11:51:53 2023

@author: 700001473
"""

from pyparsing import *


p = delimitedList(oneOf("alpha beta gamma"), '|')

r = p.parseString('alpha', parseAll=True)
print(r)

r = p.parseString('alpha|beta', parseAll=True)
print(r)

r = p.parseString('alpha, beta', parseAll=True)
print(r)
