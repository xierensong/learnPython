# coding=utf-8

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import DictVectorizer
import numpy as np

from functools import reduce
a_list = [
    {'java.util.concurrent.Executors+Executors.newFixedThreadPool': 1,
     'org.slf4j.LoggerFactory+LoggerFactory.getLogger': 1,
     'org.apache.hadoop.hbase.Cell+Cell.getFamilyArray': 1},
    {'java.util.concurrent.Executors+Executors.newFixedThreadPool': 1,
     'org.slf4j.Logger+Logger.error': 1},
    {'org.slf4j.LoggerFactory+LoggerFactory.getLogger': 1,
     'org.slf4j.Logger+Logger.warn': 1}
    ]
b_list = []
for row in a_list:
    b_list.append(reduce(lambda x, y: x + ' ' + y, row))

print(b_list)
dict_vectorizer = DictVectorizer(sparse=False)

train_tc = dict_vectorizer.fit_transform(a_list)
print('train_tc', train_tc)
vocabulary = np.array(dict_vectorizer.get_feature_names())

print('vocabulary:\n', vocabulary)

print(train_tc)


