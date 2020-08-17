#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 11:13:55 2020

@author: cnovak
"""

import requests as rq

# write to influxdb via API
# based on https://docs.influxdata.com/influxdb/v1.8/guides/write_data/

# we have started influxdb, created a database called mydb
# -> that's the URI to use when we want to write into the DB
uri = 'http://127.0.0.1:8086/write?db=mydb'

# simplest example of an entry
# 'table' + value

payload = 'cpu value=.1'
# send it
res = rq.post(uri, payload)
# response = 204 => all good
print(res)

# making the payload more complex by adding 2 attributes
payload = 'cpu,attrib1=region10,attrib2=newpc value=.1'
res = rq.post(uri, payload)
# response = 204 => all good
print(res)

