import json


api_relation_list = {}
with open('data/example.json', 'r') as json_file:
    api_relation_list = json.load(json_file)

for item in api_relation_list['method_list']:
    print(item)

node_list = []
edge_list = []

for item_dict in api_relation_list['method_list']:
    method_name = item_dict['method']
    node = '"' + str(method_name) + '"' + ' [ label="' + str(method_name) + '"]'
    print(node)
    node_list.append(node)
    api_list = item_dict['api_list']
    for api in api_list:
        api_node = '"' + str(api) + '"' + ' [ label="' + str(api) + '"]'
        node_list.append(api_node)
        edge = '"' + str(method_name) + '"' + ' -> ' + '"' + str(api) + '"'
        print('edge:', edge)
        edge_list.append(edge)

with open('data/example.dt', 'w') as dt_file:
    dt_file.write('digraph "DirectedGraph" {\n')
    dt_file.write('graph [concentrate = true];center=true;fontsize=6;'
                  'node [ color=blue,shape="box"fontsize=6,fontcolor=black,fontname=Arial];'
                  'edge [ color=black,fontsize=6,fontcolor=black,fontname=Arial];\n')
    for item in node_list:
        dt_file.write(item + '\n')
    for item in edge_list:
        dt_file.write(item + '\n')
    dt_file.write('}')
