# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 10:07:15 2012

@author: novakc
"""

import random

# This is a more advanced substitution cipher -> There are M different
# mappings; the i-th position of the string to encode is encoded according to the
# i % M -th mapping dictionary

s = "hello world, susi loves you"

M = 3

letters = 'abcdefghijklmnopqrstuvwxyz .,'

letters_list = list(letters)

enc = []
dec = []

for i in range(M):
    # this is the random shuffling of the alphabet
    random.shuffle(letters_list)
    enc.append(dict(zip(list(letters), letters_list)))
    dec.append(dict(zip(letters_list, list(letters))))


s_enc = ""

temp = [i % M for i in range(len(s))]

stemp = zip(s, temp)

for item in stemp:
    enc_table = enc[item[1]]
    s_enc += enc_table[item[0]]


print s_enc



s_dec = ""

s_enc_temp = zip(s_enc, temp)

for item in s_enc_temp:
    dec_table = dec[item[1]]
    s_dec += dec_table[item[0]]

print s_dec

