# -*- coding: utf-8 -*-

"""
Домашнее задание №4

1. Модифицировать работу со списком студентов через lambda
2. Использовать исключения для срезов и индексов. 

"""

# список с именами
students = ['Иван Петров', 'Дмитрий Петров', 'Максим Сидоров', 'Анастасия Смирнова', 'Екатерина Иванова',
            'Михаил Истомин', 'Наталья Никифорова', 'Ольга Смирнова', 'Руслан Молоков', 'Дмитрий Поляков',
            'Ольга Полякова', 'Иван Малинин', 'Ольга Колобова', 'Иван Остапченко']


# ######
# # 1. LAMBDA
# ######

# """
# выводим имя одного студента на экран:
# """
# print('выводим имя одного студента на экран:')

# input_index = input('Please enter student\'s number in range [1:'+str(len(students))+']: ')
# name_lambda = lambda input_index, lst: lst[int(input_index)-1]
# print('The student is', name_lambda(input_index, students))


# """
# выводим на экран имена нескольких студентов:
# """
# print('выводим на экран имена нескольких студентов:')

# start = input('Please enter a first number: ')
# end = input('Please enter a last number: ')

# names_func = lambda start, end, lst: lst[int(start)-1:int(end)]
# names_range = names_func(start, end, students)
# print('The students in a given range are: ', names_range)


# """
# Находим количество студентов, в именах которых есть буква "р".
# """
# print('Находим количество студентов, в именах которых есть буква "р".')

# count = 0
# count_func =  lambda students, count: [name for name in students if 'р' in name.split()[0].lower()]
# number_of_students = count_func(students, count)
# print(len(number_of_students))


######
# 2. ИСКЛЮЧЕНИЯ ДЛЯ СРЕЗОВ И ИНДЕКСОВ
######

"""
выводим имя одного студента на экран:
"""

input_index = input('Please enter student\'s number in range [1:'+str(len(students))+']: ')

try:
    converted_index = int(input_index)
    
    try:
        student = students[converted_index-1]
    
    except IndexError:
        print('EXCEPTION! There is no student with number '+str(input_index))

    else:
        print('The student is', student)

except (ValueError, NameError):
    print('Please, enter a number')