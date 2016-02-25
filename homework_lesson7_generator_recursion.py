# -*- coding: utf-8 -*-

import os
import sys
import codecs

args = sys.argv

# передаем генератору корневую папку
# проходя по списку названий файлов и папок,
# делаем полный путь и проверяем,
# если не папка, возвращаем,
# иначе снова вызываем генератор
def generator(root):
    for f in os.listdir(root):
        fullpath = os.path.join(root, f)
        if not os.path.isdir(fullpath):
            yield fullpath

        else:
            g2 = generator(fullpath)
            for fn in g2:
                yield fn


gen = generator("E:/Programming/ITMO/Python35")

# для каждого значения проверяем,
# если это текстовый файл, открываем его
# и ищем слово в строке
for item in gen:
    if item.endswith('.txt'):
        with codecs.open(item, 'r', 'utf8') as infile:
            if args[1] in infile.read():
                print("The word", args[1].upper(), "was found in file", item)
            else:
                print('Match not found.')