import networkx as nx
import operator

import matplotlib.pyplot as plt

g = nx.read_weighted_edgelist('data/edgelist24.csv')
degree = nx.degree(g)
numNodes = nx.number_of_nodes(g)
numEdges = nx.number_of_edges(g)
minDegree = min([item[1] for item in degree])
maxDegree = max([item[1] for item in degree])

print(degree)
print(numNodes)
print(numEdges)
print(minDegree)
print(maxDegree)

degreeSorted = sorted(degree, key=operator.itemgetter(1), reverse=True)
print(degreeSorted[0:9])

nx.draw(g)
plt.show()
plt.savefig('path.png')
