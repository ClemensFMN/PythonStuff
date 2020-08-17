import networkx as nx
import matplotlib.pyplot as plt

def get_level_structure(G, level):
    bfs_tree_nm1 = nx.bfs_tree(G, 1, depth_limit=level-1)
    bfs_tree_n = nx.bfs_tree(G, 1, depth_limit=level)
    return(bfs_tree_n.nodes() - bfs_tree_nm1.nodes())



G = nx.Graph()

e = [(1, 2), (1,3), (2,3), (2,4), (2,5), (3,5), (5,6), (3,7)]
G.add_edges_from(e)

# BFS traversal of the graph, starting at vertex 1
bfs_tree = nx.bfs_tree(G, 1)
print(bfs_tree.edges())

# using BFS with a depth limit

bfs_tree_1 = nx.bfs_tree(G, 1, depth_limit=1)
print(bfs_tree_1.edges())
print(bfs_tree_1.nodes())

bfs_tree_2 = nx.bfs_tree(G, 1, depth_limit=2)
print(bfs_tree_2.edges())
print(bfs_tree_2.nodes())

# we can get all vertices which have distance 2 from source vertex 0
print(bfs_tree_2.nodes() - bfs_tree_1.nodes())

res = get_level_structure(G, 2)
print(res)

res = get_level_structure(G, 3)
print(res)


nx.draw(G, with_labels = True)
plt.show()
