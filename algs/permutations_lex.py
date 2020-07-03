# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 14:06:09 2015

@author: ClNovak
"""

# based on https://en.wikipedia.org/wiki/Permutation, "Generation in lexicographic order"
# add-on info here
# http://stackoverflow.com/questions/104420/how-to-generate-all-permutations-of-a-list-in-python

def contains_sublist(lst, sublst):
    n = len(sublst)
    return any((sublst == lst[i:i+n]) for i in range(len(lst)-n+1))


def permute(a):
    stop = False

    for k in range(len(a)-2,-1,-1):
        if(a[k]<a[k+1]):
            stop = True
            break
    if(stop == True):
        for l in range(len(a)-1,k-1,-1):
            if(a[k]<a[l]):
                break
        #print("k = ", k, ", l = ", l)
        a[k], a[l] = a[l], a[k]
        a[k+1:len(a)] = a[len(a):k:-1]
        return(a)
    else:
        return("error")


def permute_gen(a):
    yield(a)
    a = permute(a)
    while(a!="error"):
        yield(a)
        a = permute(a)





a = [1,2,3]#,4,5]

sublst = [1,2]

num = 0

#if(contains_sublist(a, sublst)):
#    num += 1     

for (ind, x) in enumerate(permute_gen(a), 1):
    print(ind, x)
    if(contains_sublist(x, sublst)):
        num += 1        
        print("**********", x, num)

print(num)

#num = 1
#
#while(a!="error"):
#    print(num, a)
#    a = permute(a)
#    num += 1
