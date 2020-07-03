import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

G.add_edges_from([(1,2), (2,3), (2,4), (1,5), (5,4), (5,6), (6,8), (5,7), (7,8)])

nx.draw(G, with_labels=True)
plt.show()

print(list(G.edges))
print(G.out_edges(1))
print(G.out_edges(3))

# good illustration that BFS goes into breadth before it goes depper into the graph
print(list(nx.bfs_edges(G,1)))
print(list(nx.bfs_tree(G, 1)))
# DFS digs into the depth; only when it has reached an endpoint, it goes up and continues
print(list(nx.dfs_edges(G,1)))
print(list(nx.dfs_tree(G,1)))
