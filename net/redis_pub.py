#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 13:03:58 2021

@author: clnovak
"""

import redis

h = redis.Redis()

h.publish('chan1', 'Hello World')

