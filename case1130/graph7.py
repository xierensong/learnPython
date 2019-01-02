import networkx as nx
import pydot as pd
import random
import operator
import matplotlib.pyplot as plt
import pydot
from networkx.drawing.nx_pydot import graphviz_layout
from operator import itemgetter
from itertools import groupby
from matplotlib import cm
from numpy import linspace

# dot文件提取出pydot图（注：是列表）
p_dot = pd.graph_from_dot_file('data/temp6.dt',
                        encoding='utf-8')

print('子图数量:', len(p_dot))
# pydot图转化为networkx图
n_graph = nx.nx_pydot.from_pydot(p_dot[0])

# 输出图的简要信息
print(nx.info(n_graph))

# n_graph 节点转化为数字
n_graph4 = nx.convert_node_labels_to_integers(n_graph, label_attribute='label')
print('点:', n_graph4.nodes)
# for node in n_graph4.nodes:
#     print(node)
# 输出保存的标签值
label_dict = nx.get_node_attributes(n_graph4, 'label')
print(label_dict)
label_list = []
for item in label_dict:
    # print(item, label_list[item])
    label = {}
    label['order'] = item
    label_str = label_dict[item]
    label['class_name'] = label_str.split(',')[1].strip()
    label_list.append(label)
print(label_list)
# 分组标签
label_list.sort(key=itemgetter('class_name'))
lstg = groupby(label_list, itemgetter('class_name'))



f1 = plt.figure(figsize=(10, 10))

pos = graphviz_layout(n_graph4, prog='dot', root=0)

nx.draw(n_graph4, pos, node_size=100, alpha=0.5, with_labels=True, edge_color='black', linewidth=1.0)

# 按出度标记节点大小
# 获取出度
out_degree_list = n_graph4.out_degree
print("度:", out_degree_list)
print("大小:", [v[1] * 10 for v in out_degree_list])
# 按出度标记大小
nx.draw(n_graph4, pos, node_size=[v[1] * 100 + 100 for v in out_degree_list])

# 找团
# 有向变无向
n_graph5 = nx.to_undirected(n_graph4)
cliques = list(nx.find_cliques(n_graph5))
print('cliques for graph:')
print(cliques)
# 找中心点
ev = nx.eigenvector_centrality_numpy(n_graph5)
evSorted = sorted(ev.items(), key=operator.itemgetter(1),
                  reverse=True)
for key, val in evSorted:
    print(key, str(round(val, 2)))



# 按分组标签对结点上色
# colors = ['blue', 'black', 'grey', 'yellow', 'white', 'brown']
start = 0.0
stop = 1.0
number_of_lines= 300
cm_subsection = linspace(start, stop, number_of_lines)
colors = [cm.jet(x) for x in cm_subsection]
shapes = ['box', 'polygon', 'ellipse', 'oval', 'circle', 'egg', 'triangle', 'exagon', 'star']
i = 0
for key, group in lstg:
    node_list = []
    for g in group:
        print(key, g)
        node_list.append(g['order'])
    nx.draw_networkx_nodes(n_graph4, pos, nodelist=node_list, node_size=300,
                           node_color=colors[i])
    i = i + 1
# nx.draw_networkx_nodes(n_graph4, pos, nodelist=[10], node_size=5000)
plt.show()
filename1 = 'pic/pic.png'
f1.savefig(filename1)
