import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edges_from([(1,2,{'weight': 1}), 
                (1,3,{'weight': 3}),
                (1,4,{'weight': 2}),
                (2,3,{'weight': 1}),
                (3,4,{'weight': 2}),
                (3,5,{'weight': 3}),
                (3,6,{'weight': 5}),
                (5,6,{'weight': 1})])

length, path = nx.single_source_bellman_ford(G, source=1)

for i in range(1,7):
    print("Target = ", i, "Length= ", length[i], "Path= ", path[i])


