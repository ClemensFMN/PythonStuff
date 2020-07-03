# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 10:49:05 2012

@author: novakc
"""

from UserDict import DictMixin
import collections

class MyMultiDict(collections.MutableMapping):
    """This dict stores multiple values per key, but behaves exactly like a
    normal dict in that it returns only the newest value for any given key.

    Implementation from CNO
    """

    def __init__(self, *args, **kwargs):
        self.store = dict()
        self.update(dict(*args, **kwargs)) # use the free update to set keys

    def __getitem__(self, key):
        return self.store[key]

    def __setitem__(self, key, value):
        self.store[key] = [value]

    def __delitem__(self, key):
        del self.store[key]

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)

    def append(self, key, value):
        self.store[key].append(value)

    def dump(self):
        print self.store

class MultiDict(DictMixin):
    """ This dict stores multiple values per key, but behaves exactly like a
    normal dict in that it returns only the newest value for any given key.
    There are special methods available to access the full list of values.
    
    This implementation is based on bottle.py
    """

    def __init__(self, *a, **k):
        self.dict = dict((k, [v]) for (k, v) in dict(*a, **k).items())

    def __len__(self): return len(self.dict)
    def __iter__(self): return iter(self.dict)
    def __contains__(self, key): return key in self.dict
    def __delitem__(self, key): del self.dict[key]
    def __getitem__(self, key): return self.dict[key][-1]
    def __setitem__(self, key, value): self.append(key, value)
    def keys(self): return self.dict.keys()

    def values(self): return [v[-1] for v in self.dict.values()]
    def items(self): return [(k, v[-1]) for k, v in self.dict.items()]
    def iterkeys(self): return self.dict.iterkeys()
    def itervalues(self): return (v[-1] for v in self.dict.itervalues())
    def iteritems(self):
        return ((k, v[-1]) for k, v in self.dict.iteritems())
    def iterallitems(self):
        return ((k, v) for k, vl in self.dict.iteritems() for v in vl)
    def allitems(self):
        return [(k, v) for k, vl in self.dict.iteritems() for v in vl]

    def get(self, key, default=None, index=-1):
        ''' Return the most recent value for a key.

        :param default: The default value to be returned if the key is not
        present or the type conversion fails.
        :param index: An index for the list of available values.
        '''
        try:
            val = self.dict[key][index]
            return val
        except Exception:
            pass
        return default

    def append(self, key, value):
        ''' Add a new value to the list of values for this key. '''
        self.dict.setdefault(key, []).append(value)

    def replace(self, key, value):
        ''' Replace the list of values with a single value. '''
        self.dict[key] = [value]

    def getall(self, key):
        ''' Return a (possibly empty) list of values for a key. '''
        return self.dict.get(key) or []

    def dump(self):
        print self.dict


md = MultiDict()

md.append('a', 'alpha')
print md.get('a')

md.append('a', 'A')
print md.get('a')

md.append('a', 'Alpha')
print md.get('a')

md.append('b', 'B')
md.append('b', 'beta')
md.append('b', 'Beta')

print md.getall('a')

md.dump()

print


"*****************************************"

mmd = MyMultiDict()
mmd['a'] = 'alpha'
mmd.append('a','Alpha')

mmd['b'] = 'B'
mmd.append('b', 'Beta')

mmd.dump()

print mmd.keys()

keys = mmd.iterkeys()

for k in keys:
    print k

values = mmd.itervalues()

for v in values:
    print v

