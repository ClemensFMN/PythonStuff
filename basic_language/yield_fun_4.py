# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 21:32:07 2015

@author: ClNovak
"""

# based upon http://www.dabeaz.com/generators/Generators.pdf

import re
import itertools

f = open('yield_fun_4.txt')

ptn = r"(\d+) (\d+) (\S+)"

# group every line
grps = (re.match(ptn, line) for line in f)

# create tuples from the parsed lines
tuples = (g.groups() for g in grps)

colnames = ['col1', 'col2', 'othername']

# and convert the thing into a dict
log = (dict(zip(colnames, t)) for t in tuples)

# a generator is exhausted after one use -> use tee to generate 
# 2 generators
log1, log2 = itertools.tee(log, 2)


######################## continue with log1
# extract a column and convert it into an int
col1 = (int(c['col1']) for c in log1)

# and take the max 
max_col1 = max(col1)

print(max_col1)

######################### convert with log2


def doSomethingwithColumn(dictseq, colname, func):
    for d in dictseq:
        tmp = d[colname]
        tmpres = func(tmp)
        d[colname] = tmpres
        yield d


log_conv = doSomethingwithColumn(log2, 'col1', lambda x: 2*int(x))



for item in log_conv:
    print(item)

