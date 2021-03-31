#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 12:55:41 2021

@author: clnovak
"""

import redis

h = redis.Redis()

ps = h.pubsub()
ps.subscribe('chan1')


for m in ps.listen():
    print(m)

#res = ps.get_message()
#print(res)


