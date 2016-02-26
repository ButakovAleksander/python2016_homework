# -*- coding: utf-8-*-

import codecs
from lesson6.arithmetics import math_module
import homework_lesson1_pytohn_count

def load_data(data_file):

    data = []

    with codecs.open(data_file, 'r', 'utf8') as infile:
        for line in infile:
            data.append(line.strip())

    return data


data_file = 'lesson6/dataset.txt'
text_file = 'lesson6/file_to_search.txt'

data_list = load_data(data_file)
vector = math_module.convert_to_array(data_list)
vector_sum = math_module.do_sum(vector)
vector_mean = math_module.do_mean(vector)

word_count = homework_lesson1_pytohn_count.process_file(text_file)

print('Vector sum is', vector_sum)
print('Vector mean is', vector_mean)
print()
print('Word PYTHON occurs', word_count, 'times')


