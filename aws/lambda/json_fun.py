# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 12:12:51 2024

@author: x372924
"""

import json


f = open('data.json', 'r')
s = f.read()
prsd = json.loads(s)

for row in prsd['rows']:
    # print(row['id'], row['data'])
    fname = 'out_' + str(row['id']) + '.txt'
    f = open(fname, 'a')
    f.write(row['data'])
    f.close()

