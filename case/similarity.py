import networkx as nx

DG = nx.DiGraph([(1, 3), (1, 4), (3, 5), (5, 6)])
print(list(nx.topological_sort(DG)))
