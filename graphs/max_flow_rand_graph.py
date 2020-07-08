#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 09:01:22 2020

@author: clnovak
"""

import networkx as nx
import numpy as np
import time

strt = time.perf_counter()

RUNS = 100

Nv = 100
p = 0.1

res = []

for run in range(RUNS):

    G = nx.erdos_renyi_graph(Nv, p, directed = True)

    for e, datadict in list(G.edges.items()):
        datadict['capacity'] = 1
    
    #for e, datadict in list(G.edges.items()):
    #    print(e, datadict)
    
    
    
    f, F = nx.maximum_flow(G, 0, Nv-1)
    
    
    
    # p = nx.draw(G, with_labels=True)
    #print(f)
    res.append(f)



stp = time.perf_counter()
print(stp - strt)
