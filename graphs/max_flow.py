#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 20:34:28 2020

Create a directed graph with capacities
Obtain the maximum flow between two vertices

@author: clnovak
"""




import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

G.add_edges_from([(1,2, {'capacity':16}),
                  (1,3, {'capacity':13}),
                  (2,4, {'capacity':12}),
                  (3,2, {'capacity':4}),
                  (3,5, {'capacity':14}),
                  (4,3, {'capacity':9}),
                  (4,6, {'capacity':20}),
                  (5,4, {'capacity':7}),
                  (5,6, {'capacity':4})])

for e in list(G.edges):
    print(e)

for e, datadict in list(G.edges.items()):
    print(e, datadict, datadict['capacity'])

# f is the max flow between 1 & 6
# F contains the actual flows between nodes of the max-flow solution
f, F = nx.maximum_flow(G, 1, 6)


# p=nx.draw(G, with_labels=True)
pos = nx.spring_layout(G, seed=7)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos)
edge_labels = nx.get_edge_attributes(G, "capacity")
nx.draw_networkx_edge_labels(G, pos, edge_labels)
