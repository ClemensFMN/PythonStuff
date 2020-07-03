# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 18:37:38 2015

@author: cnovak
"""

import itertools as iter
from operator import itemgetter


orders = [{'Customer': 'Clemens', 'Product': 'MacBook', 'Price': 1000, 'Qty': 2},
          {'Customer': 'Susi', 'Product': 'Book', 'Price': 60, 'Qty': 3},
          {'Customer': 'Strolchi', 'Product': 'Notebook', 'Price': 700, 'Qty': 1},
          {'Customer': 'Clemens', 'Product': 'USB Stick', 'Price': 15, 'Qty': 4}]


sorted_orders = sorted(orders, key=itemgetter('Customer'))

res = iter.groupby(orders, key=itemgetter('Customer'))



