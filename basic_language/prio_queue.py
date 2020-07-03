# -*- coding: utf-8 -*-
"""
Created on Fri Apr 04 13:05:54 2014

@author: novakc
"""

import heapq as hq


# simple priority queue based on stdlib's heapq

h = []

# store tuples (prio, item)

hq.heappush(h, (5, 'write code'))
hq.heappush(h, (7, 'release product'))
hq.heappush(h, (1, 'write spec'))
hq.heappush(h, (3, 'create tests'))

# items get popped based on prio (lowest first)
print hq.heappop(h)
print hq.heappop(h)



