# coding=utf-8

import numpy as np

a_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print('a list', a_list)

a_array = np.array(a_list)

print('a array', a_array)

a_new_list = a_array.tolist()

print('a new list', a_new_list)