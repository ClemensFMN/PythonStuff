# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 08:30:43 2023

@author: 700001473
"""

from pyparsing import *


def chkGrammar(grm, str, strict = False):
    res = grm.parseString(str, parse_all=strict)
    print(res)
    for (k,v) in res.items():
        print("key: ", k, "value: ", v)



n = Word(nums, max=5)
l = Word(alphas, max=3)

grm = n("num") | l("letter")


chkGrammar(grm, "123")
chkGrammar(grm, "12345")
# if we use parse_all=True, then strings which do not match cause an exception
chkGrammar(grm, "123456", strict=False)

chkGrammar(grm, "abc")

print("*****************")

grm = l("varname") + ":" + n("value")
chkGrammar(grm, "abc: 45")


