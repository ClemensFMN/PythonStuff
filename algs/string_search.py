# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 15:28:25 2012

@author: novakc
"""


def exact_search(s, s_search):
    found_positions = []
    # we iterate over the string s
    for i in range(len(s)-  len(s_search) + 1):

        found = 0
        #print s[i]
    
        # and for every string position in s we start comparing s and s_search
        for j in range(len(s_search)):
            #print '...', s_search[j]
            # if there is a mismatch we break the comparison
            if s_search[j] != s[i+j]:
                found = 1
                #print 'giving up...'
                break

        if found == 0:
            #print "found:", i
            found_positions.append(i)
    return found_positions


def fuzzy_search(s, s_search, metric_threshold):
    found_positions = []
    # we iterate over the string s
    for i in range(len(s)-  len(s_search) + 1):

        metric = 0

        # and for every string position in s we start comparing s and s_search
        for j in range(len(s_search)):
            # sum up the metric difference for every character
            metric += abs(ord(s_search[j]) - ord(s[i+j]))

        print metric
        # if the metric is below a threshold, we have found a match
        if metric < metric_threshold:
            #print "found:", i
            found_positions.append(i)
    return found_positions




# The big string
s = "susi loves ham and eggs and likes getting drunk with beer loves"

# we search for this string
s_search = "loves"


pos = exact_search(s, s_search)
print pos

s = "loves, lives, likes"

pos = fuzzy_search(s, s_search, 10)
print pos



