# -*- coding: utf-8 -*-

"""
№1

1. Найти в данной папке все файлы, в которых содержится слово python, и вывести на
экран имена файлов.
2. Посчитать общее количество найденных слов и вывести на экран
3. Записать в файл "result.txt" список найденных файлов и число найденных слов python
"""

import os
import codecs
from os.path import join


def process_file(filename):

    search_string = 'python'
    count = 0

    with codecs.open(filename, 'r', 'utf8') as infile:
        text = infile.read().split()
        for i in text:
            if search_string == i.strip():
                count += 1
    return count


def crawl_folder(folder_name):

    total_python_count = 0
    valid_files = []

    for root, dirs, files in os.walk(folder_name):

        for filename in files:
            if filename.endswith('.txt'):

                current_count = process_file(join(root, filename))
                total_python_count += current_count

                if current_count != 0:
                    valid_files.append(join(root, filename))


    return total_python_count, valid_files

search_folder = '../homework/lesson1'
count, valid_files = crawl_folder(search_folder)

print('Общее количество найденных слов: ', count)

with codecs.open(r'../homework/lesson1/results.txt', 'w', 'utf8') as out:
    for n in valid_files:
        out.write(n+'\n')
    out.write('Общее количество найденных слов: '+str(count))