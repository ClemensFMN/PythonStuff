# -*- coding: utf-8 -*-
"""
Created on Tue May 24 08:28:04 2016

@author: ClNovak
"""

s="""abcDEFGhigghEbkWalDorkFtyAwaldORmFtsimrLqsrcbyoArBeDeyvKlcbqwikomkstrEBGadhrbyUiqlxcnBjf"""

# the crossword has 11 rows
M = 11
# and 8 rows
N = 8


def conv_s_dict(s):
    i=0
    j=0

    dct = {}
    
    for e in s:
        pos = (i,j)
        dct[pos] = e
        #print(pos, e)
        i+=1
        if(i==11):
            i=0
            j+=1

    return(dct)


def gen_index_1(lngth, deltax, deltay, x0, y0):
    n = range(lngth)
    ind = [(deltax*x+x0,deltay*x+y0) for x in n]
    return(ind)

def get_s_from_ind(s, ind):
    tmp = [s[i] for i in ind]
    return("".join(tmp))



dct = conv_s_dict(s)

ind1 = gen_index_1(5,1,0,5,1)

print(ind1)

res = get_s_from_ind(dct, ind1)

print(res)


