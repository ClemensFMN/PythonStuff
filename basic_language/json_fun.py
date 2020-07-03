# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 15:28:27 2012

@author: novakc
"""

import json

lst = ["hello", "this", "is a list", 45, 78]
mp = {"a":5, "c":10}


#print l

print json.dumps(lst)
print json.dumps(mp)
