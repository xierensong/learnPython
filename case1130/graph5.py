import networkx as nx
import pydot as pd
import operator
import matplotlib.pyplot as plt
import pydot
from networkx.drawing.nx_pydot import graphviz_layout

# dot文件提取出pydot图（注：是列表）
p_dot = pd.graph_from_dot_file('data/temp.dt',
                        encoding='utf-8')
# print(p_dot[0])
# png_path = "pic/test.png"
# pydot图输出为png图片
# p_dot[0].write_png(png_path)

# pydot图转化为networkx图
n_graph = nx.nx_pydot.from_pydot(p_dot[0])

# print(n_graph)
print('节点数：', nx.number_of_nodes(n_graph))
print('边数：', nx.number_of_edges(n_graph))

degree = nx.degree(n_graph)
print('最小度数：', min([item[1] for item in degree]))

print('最大度数：', max([item[1] for item in degree]))

degreeSorted = sorted(degree, key = operator.itemgetter(1), reverse=True)
print('前n大度数节点：', degreeSorted[0:9])

n_graph2 = n_graph.copy()
d2 = nx.degree(n_graph2)

for n in list(n_graph2.nodes()):
    if d2[n] <= 1:
        n_graph2.remove_node(n)

print('节点数：', nx.number_of_nodes(n_graph2))
print('边数：', nx.number_of_edges(n_graph2))

degree = nx.degree(n_graph2)
print('最小度数：', min([item[1] for item in degree]))

print('最大度数：', max([item[1] for item in degree]))

degreeSorted = sorted(degree, key = operator.itemgetter(1), reverse=True)
print('前n大度数节点：', degreeSorted[0:9])

# 输出图的简要信息
print(nx.info(n_graph))

# 有向图转化为无向图
n_graph3 = nx.to_undirected(n_graph)
print('是否连通：', nx.number_connected_components(n_graph3))
print('子图个数：', nx.number_connected_components(n_graph3))
node_list = nx.nodes(n_graph)
print(type(node_list))
for item in node_list:
    print("werqwe:", item, type(item))
# print(node_list[0])

G = nx.complete_graph(5)
node_list1 = nx.nodes(G)
print(type(node_list1))
for item in node_list1:
    print("werqwe:", item, type(item))
f1 = plt.figure(figsize=(10, 10))
pos = graphviz_layout(G)
nx.draw(G, pos)
plt.show()
png_path = "pic/test.png"
f1.savefig(png_path)

# n_graph 节点转化为数字
n_graph4 = nx.convert_node_labels_to_integers(n_graph, label_attribute='label')

f1 = plt.figure(figsize=(10, 10))
# pos = nx.spring_layout(n_graph2)
# dot − filter for drawing directed graphs
# neato − filter for drawing undirected graphs
# twopi − filter for radial layouts of graphs
# circo − filter for circular layout of graphs
# fdp − filter for drawing undirected graphs
# sfdp − filter for drawing large undirected graphs
# patchwork − filter for squarified tree maps
# osage − filter for array-based layouts
print(n_graph4)
pos = graphviz_layout(n_graph4, prog='dot', root=0)

nx.draw(n_graph4, pos, node_size=400, alpha=0.5, with_labels=True)
plt.show()
filename1 = 'pic/graphLabels.png'
f1.savefig(filename1)

