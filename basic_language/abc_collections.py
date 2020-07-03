# -*- coding: utf-8 -*-
"""
Created on Thu Mar 06 17:18:33 2014

@author: NovakC
"""

# http://stackoverflow.com/questions/3387691/python-how-to-perfectly-override-a-dict

import collections


class TransformedDict(collections.MutableMapping):
    """A dictionary that applies an arbitrary key-altering
       function before accessing the keys"""

    def __init__(self, *args, **kwargs):
        self.store = dict()
        self.update(dict(*args, **kwargs))  # use the free update to set keys

    def __getitem__(self, key):
        return self.store[self.__keytransform__(key)]

    def __setitem__(self, key, value):
        self.store[self.__keytransform__(key)] = value

    def __delitem__(self, key):
        del self.store[self.__keytransform__(key)]

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)

    def __keytransform__(self, key):
        return key

    def __repr__(self):
        s = ''
        for k,v in self.iteritems():
            s = s + str(k) + '->' + str(v) + "\n"
        return s

td = TransformedDict()

td['A'] = 7
td['B'] = 4

for k,v in td.iteritems():
    print k,'->',v

print td.__len__()
print "X"
print td
print "X"

