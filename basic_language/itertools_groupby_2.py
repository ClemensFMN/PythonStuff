# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 07:19:46 2015

@author: ClNovak
"""

import itertools as it
import operator as op

# have a list of maps

orders =[{'Customer': 'Clemens', 'Product': 'A', 'Price': 10, 'Qty': 2},
         {'Customer': 'Susi', 'Product': 'B', 'Price': 100, 'Qty': 4},
         {'Customer': 'Clemens', 'Product': 'C', 'Price': 20, 'Qty': 5},
         {'Customer': 'Clemens', 'Product': 'A', 'Price': 3, 'Qty': 1}]

# before groupby works (as intended here), sorting is needed
sorders = sorted(orders, key=op.itemgetter('Customer'))

# now group by customer
grpdorders = it.groupby(sorders, key=op.itemgetter('Customer'))

#
for k,v in grpdorders:
    #print(k,v)
    # the group contains the group key and a list of maps
    # from each map extract price and qty and multiply these values
    total = map(lambda x: x['Price'] * x['Qty'], v)
    # and output them
    print(k, list(total))

