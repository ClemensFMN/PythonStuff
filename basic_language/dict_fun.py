# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 08:39:14 2012

@author: novakc
"""

import random

#a very basic cryptography algorithm based on substitution
# we have two dictionaries:
# enc_dict = ['a':'v', 'b':d' ...]
# is the mapping from the alphabet letters to the encoded ones
# & dec_dict is the other way round

s = "hello world, susi loves you"



letters = 'abcdefghijklmnopqrstuvwxyz .,'

letters_list = list(letters)

# this is the random shuffling of the alphabet
random.shuffle(letters_list)

# here we create a dict by zipping the alphabet with the shuffled version
# -> allows efficient encoding
enc_dict = dict(zip(list(letters), letters_list))

# here we create the reversed dict which allows efficient decoding...
dec_dict = dict(zip(letters_list, list(letters)))

print(enc_dict)

s_enc = ""

# strings are iterable - for every char we perform a dict lookup
for item in s:
    s_enc += enc_dict[item]

print(s_enc)

s_dec = ""

for item in s_enc:
    s_dec += dec_dict[item]

print(s_dec)

