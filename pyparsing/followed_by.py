# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 12:12:06 2023

@author: 700001473
"""

from pyparsing import *

# https://stackoverflow.com/questions/30918013/non-greedy-list-parsing-with-pyparsing

word = Word(alphas)
grammar = Group(OneOrMore(word + FollowedBy(word*2)))("first") + word("penultimate") + word("ultimate")

s = "one two three four"

res = grammar.parseString(s)
print(res)


grammar = Group(OneOrMore(word) + FollowedBy('999'))("first") + Literal('999')
s = '''vlf dvdsv
999'''

res = grammar.parseString(s)
print(res)




