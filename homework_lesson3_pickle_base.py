# -*- coding: utf-8 -*-

"""
Сделайте простую базу данных.
При первом запуске программы, она создает файл pickle с данными.
При последующих открывает этот файл и выводит на экран содержимое.

3.* Реализовать поиск/фильтрацию в базе данных - то есть вывод по условию.
"""

import pickle
import os

data = {
        'a': [1, 2.0, 3, 4+6j],
        'b': ("character string", b"byte string"),
        'c': {None, True, False}
        }

dataset = 'lesson3/data.pickle'

if not os.path.exists(dataset):
    with open('lesson3/data.pickle', 'wb') as f:
        pickle.dump(data, f)
else:
    with open(dataset, 'rb') as f:
        data_new = pickle.load(f)

condition = 'c'
for k, v in data_new.items():
    if k == condition:
        print(v)
