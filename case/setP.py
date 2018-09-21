# code=utf-8

import csv

lib_set = set()

with open('../data/project_lib.txt', 'r', newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print('x', row)
        row = (row['groupId'], row['artifactId'], row['version'])
        lib_set.add(row)
    print('csv len:', reader.line_num)

print('lib len:', len(lib_set))
for set_element in lib_set:
    print('y', set_element)


