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


pos = nx.spring_layout(G)
nx.draw_networkx(G, pos)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()
