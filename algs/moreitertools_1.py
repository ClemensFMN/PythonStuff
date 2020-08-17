#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 15:33:50 2020

@author: clnovak
"""

import more_itertools as mi

x = [1,2,3,4,5,6]
y = mi.windowed(x, 3, step = 4)

print(list(y))
