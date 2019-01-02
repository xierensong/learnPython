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
p_dot = pd.graph_from_dot_file('data/han.dt',
                        encoding='utf-8')

# pydot图转化为networkx图
n_graph = nx.nx_pydot.from_pydot(p_dot[0])

# 输出图的简要信息
print(nx.info(n_graph))

# multiDiGraph 转化为 DiGraph
n_graph1 = nx.DiGraph(n_graph)

# n_graph 节点转化为数字
n_graph4 = nx.convert_node_labels_to_integers(n_graph1, label_attribute='label')

print('点:', n_graph4.nodes)
# for node in n_graph4.nodes:
#     print(node)
# 输出保存的标签值
label_dict = nx.get_node_attributes(n_graph4, 'label')

print('标签 ', label_dict)

# 按出度标记边权重

# 获取出度
out_degree_list = n_graph4.out_degree
print("度:", out_degree_list)

# 按出度标记边权重
weight_dict = {}
for node in out_degree_list:
    out_degree = node[1]
    if out_degree != 0:
        # 权重放大1000倍，避免小数计算
        weight = 1000 // out_degree
        out_edge_list = nx.edges(n_graph4, nbunch=node[0])
        # print(out_edge_list)
        # 修改(u,v)为(u,v,key)
        # out_edge_key_list = []
        # for key, edge in enumerate(nx.edges(n_graph4)):
        #     for out_edge in out_edge_list:
        #         if edge == out_edge:
        #             tmp_out_edge_list = list(edge)
        #             tmp_out_edge_list.append(key)
        #             out_edge_key = tuple(tmp_out_edge_list)
        #             # print(out_edge_key)
        #             out_edge_key_list.append(out_edge_key)
        # for edge in out_edge_key_list:
        for edge in out_edge_list:
            weight_dict[edge] = weight
# print(weight_dict)

# 设置边权重
nx.set_edge_attributes(n_graph4, weight_dict, 'weight')

# 打印权重信息
print('edge weight list:')
edge_list = nx.edges(n_graph4)
print(nx.get_edge_attributes(n_graph4, 'weight'))
# for edge in edge_list:
#     print(', '.join(list(edge[0], edge[1], nx.get_edge_attributes(n_graph4, weight)weight'])))

# 计算两点最短路径
paths = list(nx.shortest_simple_paths(n_graph4, 0, 222))
print("路径 ", paths)






