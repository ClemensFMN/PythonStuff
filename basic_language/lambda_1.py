# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 15:16:26 2012

@author: novakc
"""

data = ['susi', 'sumsi', 'wolfgang', 'peter']

values = [10,5,12,8]

data_full = zip(data, values)

for item in data_full:
    print item

m_value = min(data_full, key = lambda s: s[1])

print 'Minimum object:', m_value

sorted_data_full = sorted(data_full, key = lambda s: s[1])

print 'Sorted list:', sorted_data_full


