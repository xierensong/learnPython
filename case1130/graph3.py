import random
import networkx as nx
"""
networkx图 转换成 graphviz dot图
"""

# 生成networkx图
G = nx.petersen_graph()
# networkx图转化为pydot图
pdot = nx.nx_pydot.to_pydot(G)

shapes = ['box', 'polygon', 'ellipse', 'oval', 'circle', 'egg', 'triangle', 'exagon', 'star', ]
colors = ['blue', 'black', 'red', '#db8625', 'green', 'gray', 'cyan', '#ed125b']
styles = ['filled', 'rounded', 'rounded, filled', 'dashed', 'dotted, bold']

# 设置pydot图点的属性
for i, node in enumerate(pdot.get_nodes()):
    node.set_label("n%d" % i)
    node.set_shape(shapes[random.randrange(len(shapes))])
    node.set_fontcolor(colors[random.randrange(len(colors))])
    node.set_fillcolor(colors[random.randrange(len(colors))])
    node.set_style(styles[random.randrange(len(styles))])
    node.set_color(colors[random.randrange(len(colors))])

# 设置pydot图边的属性
for i, edge in enumerate(pdot.get_edges()):
    edge.set_label("e%d" % i)
    edge.set_fontcolor(colors[random.randrange(len(colors))])
    edge.set_style(styles[random.randrange(len(styles))])
    edge.set_color(colors[random.randrange(len(colors))])

png_path = "test.png"
# 输出pydot图的png版本
pdot.write_png(png_path)
# 输出pydot的内容
print(pdot)

# pydot图转化为networkx图
nG = nx.nx_pydot.from_pydot(pdot)
# 打印networkx图的节点
for x in nx.nodes(nG):
    print(x)
# 打印network图的边
for x in nx.edges(nG):
    print(x)
# 打印networkx图的点的度数：
for n, x in G.degree():
    print(n, x)
# 打印networkx图的聚类：
print(nx.clustering(G))
