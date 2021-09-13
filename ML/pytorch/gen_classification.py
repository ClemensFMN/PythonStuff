import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification

X, Y = make_classification(n_samples=20, n_features=2, n_redundant=0, n_informative=1,
                             n_clusters_per_class=1)

plt.scatter(X[:, 0], X[:, 1], marker='o', c=Y, s=25, edgecolor='k')
plt.show()

