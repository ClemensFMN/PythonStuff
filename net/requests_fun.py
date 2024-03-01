# -*- coding: utf-8 -*-
"""
Created on Wed May  3 09:21:35 2023

@author: 700001473
"""

import requests

#r = requests.get('http://httpbin.org/get')
#print(r.status_code)
#print(r.headers)
#print(r.json())


#r = requests.post('http://httpbin.org/post')
#print(r.status_code)
#print(r.headers)
#print(r.json())


# r = requests.post('http://httpbin.org/post', params={'param1': 45, 'param2': 12})
# print(r.status_code)
# print(r.headers)
# print(r.json())
# print(r.json()['args']['param1'])

# this is now in data
# r = requests.post('http://httpbin.org/post', params={'param1': 45, 'param2': 12}, data="mickimaus")
# print(r.status_code)
# print(r.headers)
# print(r.json())


# this is now in form as JSON
# r = requests.post('http://httpbin.org/post', params={'param1': 45, 'param2': 12}, data={'field1':'abc', 'field2': 34})
# print(r.status_code)
# print(r.headers)
# print(r.json())



files = {'file': open('requests_fun.py', 'r')}
r = requests.post('http://httpbin.org/post', files=files)
print(r.status_code)
print(r.headers)
print(r.json())

