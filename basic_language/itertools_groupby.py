# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 12:55:46 2012

@author: novakc
"""

import itertools as it
import re

# run length encoding of this string
s = "aaabbbbaacccccddddddddddddd"


RLE_list = ''

# for every group we get the key which is the char in our case)
# and an iterator
for k, g in it.groupby(s):
    # how many items do we have in the group?    
    length = len(list(g))
    print(k, length)
    # add the char
    RLE_list += str(k)
    # and the number of times it appears to the RLE string
    RLE_list += str(length)


print()

print(RLE_list)

# parse the RLE string
# it contains of a list of (char + number)
s_parsed = re.findall(r"([a-z])(\d*)", RLE_list)

# the result is a list of (char, number) tuples
print(s_parsed)

s_decode = ""

for item in s_parsed:
    # now expand the char by the number of times it appears
    temp = item[0] * int(item[1])
    # and add it to the decoded string
    s_decode += temp


print(s_decode)

assert(s == s_decode)