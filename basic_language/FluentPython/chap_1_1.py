#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 11:15:20 2019

@author: clnovak
"""

import collections


# let's design a collection holding 1A...1D, 2A...2D,...9A...9D

itm = collections.namedtuple('Itm', ['number', 'letter'])


class MyColl:
    def __init__(self):
        self._cards = [itm(n,l) for n in range(1,10)
                                for l in list('ABCD')]

    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, pos):
        return self._cards[pos]



myc1 = itm(3,'C')
print(myc1)

deck = MyColl()
print(len(deck))


for itm in deck:
    print(itm)


print(myc1 in deck)





