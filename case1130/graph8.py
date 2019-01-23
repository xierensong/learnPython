import networkx as nx
import pydot as pd
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout
import re
import logging
from pathlib import Path
import json
from pprint import pprint

print('从文件中提取pydot图...')
# dot文件提取出pydot图（注：是列表）13 maven 11 9 ant 7 derby
p_dot = pd.graph_from_dot_file('data/example.dt',
                               encoding='utf-8')

print('子图数量:', len(p_dot))
logging.debug('子图数量:' + str(len(p_dot)))

print('pydot图转化为networkx图...')
# pydot图转化为networkx图
n_graph = nx.nx_pydot.from_pydot(p_dot[0])

# 输出图的简要信息
print(nx.info(n_graph))
logging.debug(nx.info(n_graph))

print('复制新图...')
# multiDiGraph 转化为 DiGraph
# n_graph1 = nx.DiGraph(n_graph)
n_graph1 = n_graph.copy()
print('复制图完成.')

# n_graph 节点转化为数字
n_graph4 = nx.convert_node_labels_to_integers(n_graph, label_attribute='label')
print('点:', n_graph4.nodes)

# # 查找有向图中的环
# print('环个数 ', len(list(nx.simple_cycles(n_graph1))))
#
# # 去掉自环
# self_loop = list(nx.selfloop_edges(n_graph1))
# print('单环个数 ', len(self_loop))
# print('删除单环')
# n_graph1.remove_edges_from(self_loop)
#
# # 查找有向图中的环
# print('环个数 ', len(list(nx.simple_cycles(n_graph1))))
#
# 去掉非自环
# while 1:
#     try:
#         edge_list = list(nx.find_cycle(n_graph4, orientation='original'))
#         print('自环边 ', edge_list)
#         del_edge = edge_list[-1]
#         n_graph4.remove_edges_from([(del_edge[0], del_edge[1])])
#     except nx.NetworkXNoCycle:
#         print('没有环')
#         break
#
# # 查找有向图中的环
# print('环', len(list(nx.simple_cycles(n_graph4))))
# print(nx.info(n_graph4))

# 找某个节点的为root的子图
# 找某个节点下的所有子孙节点
# root 75
node_list = set()
root = 90
node_list.add(root)

def dfs(root):
    out_list = n_graph4.successors(root)
    for item in out_list:
        print('item:', item)
        node_list.add(item)
        dfs(item)


dfs(root)

# 根据节点画出子图
n_graph5 = n_graph4.subgraph(node_list)

# print("节点集：", nx.get_node_attributes(n_graph5, 'label'))
pprint(nx.get_node_attributes(n_graph5, 'label'))
print(nx.info(n_graph5))
f1 = plt.figure(figsize=(10, 10))
pos = graphviz_layout(n_graph5, prog='dot', root=0)
nx.draw(n_graph5, pos, node_size=100, alpha=0.5, with_labels=True, edge_color='black', linewidth=1.0)
plt.show()
filename1 = 'pic/pic.png'
f1.savefig(filename1)
