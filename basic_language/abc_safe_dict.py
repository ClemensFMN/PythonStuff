# -*- coding: utf-8 -*-
"""
Created on Thu Mar 06 18:16:29 2014

@author: NovakC
"""

class SafeDict(collections.MutableMapping):
    """A 'safe' dictionary"""

    def __init__(self, *args, **kwargs):
        self.store = dict()
        self.update(dict(*args, **kwargs))  # use the free update to set keys

    def __getitem__(self, key):
        try:
            return self.store[key]
        except KeyError:
            return 0.0  # safety net...

    def __setitem__(self, key, value):
        self.store[key] = value

    def __delitem__(self, key):
        del self.store[key]

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)


sd = SafeDict()

sd['A'] = 7
sd['B'] = 4

for k,v in sd.iteritems():
    print k,'->',v

# safety net in action
print sd['C']
