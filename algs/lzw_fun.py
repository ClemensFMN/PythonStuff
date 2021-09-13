# -*- coding: utf-8 -*-
"""
Created on Fri Apr 04 09:37:09 2014

@author: novakc
"""

# http://rosettacode.org/wiki/LZW_compression#Python

def compress(uncompressed):
    """Compress a string to a list of output symbols."""
 
    # Build the dictionary.
    dict_size = 58
    dictionary = dict((chr(i), chr(i)) for i in range(65, 65 + dict_size))
    dictionary[' '] = ' '

    w = ""
    result = []
    for c in uncompressed:
        #print "****************** " + c
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            # Add wc to the dictionary.
            dictionary[wc] = dict_size
            dict_size += 1
            w = c
 
        #print dictionary
    # Output the code for w.
    if w:
        result.append(dictionary[w])
    return result
 
 
def decompress(compressed):
    """Decompress a list of output ks to a string."""
 
    # Build the dictionary.
    dict_size = 58
    dictionary = dict((chr(i), chr(i)) for i in range(65, 65 + dict_size))
    dictionary[' '] = ' '

    w = result = compressed.pop(0)
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: %s' % k)
        result += entry
 
        # Add w+entry[0] to the dictionary.
        dictionary[dict_size] = w + entry[0]
        dict_size += 1
 
        w = entry
    return result
 
 

s = 'TOBEORNOTTOBEORTOBEORNOT'
compressed = compress(s)
print (compressed)
decompressed = decompress(compressed)
print (decompressed)