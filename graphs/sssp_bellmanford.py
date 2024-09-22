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

pos = nx.spring_layout(G, seed=7)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos)
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)

length, path = nx.single_source_bellman_ford(G, source=1)



for i in range(1,7):
    print("Target = ", i, "Length = ", length[i], "Path = ", path[i])


