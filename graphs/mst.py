import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edges_from([(1,2,{'weight': 1}), (2,3,{'weight': 1}), (1,3,{'weight': 10}), (3,4,{'weight': 1})])

#nx.draw(G, with_labels=True)
#plt.show()

T = nx.minimum_spanning_tree(G, weight='weight')
print(sorted(T.edges))
