# unconstrained KNapsack problem
import numpy as np

wvec = [2, 3]
vvec = [3, 5]


Wtotal = 10


# a vector which holds at position i the maximum value of the 
# knapsack with weight i
mvec = np.zeros(Wtotal+1)

items = {}

# total weight = 0 -> total value = 0
mvec[0] = 0
items[0] = []


# we look at knapsacks with increasing weight
for w in range(1, Wtotal+1):

    cand = [(-1, mvec[w-1])]

    # go over all items
    for (ind, vi, wi) in zip(range(len(wvec)), vvec, wvec):

        # if the i-th item fits in the knapsack ...
        if(w - wi > -1):
            # ... calculate the new total value and add it to the candidate list
            # if no item would fit in, we continue with the previous value 
            # (see the line cand = [(-1, mvec[w-1])] )
            cand.append((ind, vi + mvec[w-wi]))

    # take the max over all candidates as final value & retrieve the index of 
    # the item we took
    ind, mvec[w] = max(cand, key=lambda x:x[1])

    # if the index is -1, we haven't added anything -> the new items are 
    # the same ones as before (at w-1)
    if(ind == -1):
        #print w, "nothing added; previous content", w-1
        items[w] = items[w-1]
    else:
        # otherwise we added an item ind
        #print w, "added item", ind, "previous content from",  w-wvec[ind]
        # to the previous content at w-wvec[ind]
        # some magic to obtain a copy of the list at items[w-wvec[ind]]
        previous_content = list(items[w-wvec[ind]])
        # set the 
        items[w] = previous_content
        items[w].append(ind)

    #print w, items

print

for ind in range(Wtotal+1):
    
    print(ind, items[ind], '-->', mvec[ind])
