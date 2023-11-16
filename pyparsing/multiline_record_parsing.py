# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 15:20:01 2023

@author: 700001473
"""

from pyparsing import *

# multiline parsing
# we have a file with several 
# maybe this is interesting as well? https://stackoverflow.com/questions/40697006/multiline-pyparsing-example


# let's assume that our Kundennummer starts with a fixed string 1000K followed by 3 integers
kdnr = Literal('1000K') + Word(nums, exact=3)


kdnr_test = "1000K123"

# parse a string, we need this parseAll option to throw an exception when the string cannot be fully matched
res = kdnr.parseString(kdnr_test, parseAll=True)
print(res)


# now let's consider a record with three lines
# kundennummer
# somet hing
# 999

# this work only with two "words" as in the example above
# newlines are ignored, so there can be several empty lines eg between kundenummer & the next line
# however, != 2 words cause a parsing error
# record = kdnr + Word(alphanums) + Word(alphanums) + Literal('999')


# match several chunks of letters + numbers
# this does not work as OneOr... accepts the 999 as well and the Literal('999') 
# cannot be matched anymore => error
# record = kdnr + OneOrMore(Word(alphanums)) + Literal('999')

# this seems to be a partial solution: *NOT* a 999 and OneOrMore words consisting of alphanums
# for unkown reasons, it parese the 999 at the end as well?
# remainder = ~Literal('999') + OneOrMore(Word(alphanums))
# this includes the 999 in the match - not ideal, especially when matching several records :-( (see below)
# record = kdnr + remainder
# this does not work - expected 999
# record = kdnr + remainder + Literal('999')


# remainder = ~Literal('999') + OneOrMore(Word(alphanums)) + FollowedBy('999')
# record = kdnr + remainder


# this works with alphas but not alphanums??
garbage = Group(OneOrMore(Word(alphas)) + FollowedBy('999'))("garbage")
record = kdnr + garbage + Literal('999')

# record = kdnr + Group(OneOrMore(Word(alphanums))) + Literal('999') + StringEnd()


record_test='''1000K345 
dfdfsdf dsfsdf dsvfdb
999
'''

# pyparsing seems to ignore the newlines in between => this is good :-)
# if our kundenummer has > 3 digits, this throws some error...
res = record.parseString(record_test)
print(res)

# file = OneOrMore(Group(record))

# file_test = '''
# 1000K123
# 4567 dklvjldvj
# 999
# 1000K456
# 23543 dklvjldvj
# 999
# '''

# res = file.parseString(file_test)
# print(res)


