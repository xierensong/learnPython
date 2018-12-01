import random
import networkx as nx
"""
networkx图 转换成 graphviz dot图
"""

G = nx.petersen_graph()
pdot = nx.drawing.nx_pydot.to_pydot(G)

shapes = ['box', 'polygon', 'ellipse', 'oval', 'circle', 'egg', 'triangle', 'exagon', 'star', ]
colors = ['blue', 'black', 'red', '#db8625', 'green', 'gray', 'cyan', '#ed125b']
styles = ['filled', 'rounded', 'rounded, filled', 'dashed', 'dotted, bold']

for i, node in enumerate(pdot.get_nodes()):
    node.set_label("n%d" % i)
    node.set_shape(shapes[random.randrange(len(shapes))])
    node.set_fontcolor(colors[random.randrange(len(colors))])
    node.set_fillcolor(colors[random.randrange(len(colors))])
    node.set_style(styles[random.randrange(len(styles))])
    node.set_color(colors[random.randrange(len(colors))])

for i, edge in enumerate(pdot.get_edges()):
    edge.set_label("e%d" % i)
    edge.set_fontcolor(colors[random.randrange(len(colors))])
    edge.set_style(styles[random.randrange(len(styles))])
    edge.set_color(colors[random.randrange(len(colors))])

png_path = "test.png"
pdot.write_png(png_path)
print(pdot)