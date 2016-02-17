# -*- coding: utf-8 -*-

"""
Домашнее задание №2

"""

# список с именами
students = ['Иван Петров', 'Дмитрий Петров', 'Максим Сидоров', 'Анастасия Смирнова', 'Екатерина Иванова',
            'Михаил Истомин', 'Наталья Никифорова', 'Ольга Смирнова', 'Руслан Молоков', 'Дмитрий Поляков',
            'Ольга Полякова', 'Иван Малинин', 'Ольга Колобова', 'Иван Остапченко']

"""
выводим имя одного студента на экран:
"""

# input_index = input('Please enter student\'s number in range [1:'+str(len(students))+']: ')
#
# if input_index.isdigit():
#     if int(input_index) <= len(students):
#         print('The student is', students[int(input_index)-1])
#     else:
#         print('There is no student number '+input_index)
# else:
#     print('It seems you entered something else but not a number. Try again.')


"""
выводим на экран имена нескольких студентов:
"""

# start = input('Please enter a first number: ')
# end = input('Please enter a last number: ')
#
# if start.isdigit() and end.isdigit():
#     if int(start) > 0 and int(end) <= len(students):
#         print('The students in a given range are: ', students[int(start)-1:int(end)])
#
#     else:
#         print('Invalid range')
# else:
#     print('Invalid input')


"""
Находим количество студентов, в именах которых есть буква "р".
"""
# count = 0
# for name in students:
#     if 'р' in name.split()[0].lower():
#         count += 1
#
# print(count)


"""
Находим группы студентов с одинаковыми именами и создаем списки этих групп.
"""

temp_list = []
for name in students:
    current_name = []
    name = name.split()
    current_name.append([name[0], [name[1]]])
    temp_list.append(current_name)

###### list version

# all_names = []
# firstnames = set([''.join(name[0][0]) for name in temp_list])
# for x in firstnames:
#     current_name = []
#     for y in temp_list:
#         name_string = ''.join(y[0][0])
#         if name_string == x:
#             current_name.append(y[0][1])
#             all_names.append([name_string, current_name])
#
# print(all_names)


####### dict version

# names_dict = {}
# for name in temp_list:
#     if not name[0][0] in names_dict:
#         names_dict[name[0][0]] = [name[0][1]]
#     else:
#         names_dict[name[0][0]].append(name[0][1])
#
# # выводим только те имена, которым соответствует больше одной фамилии
# for k, v in names_dict.items():
#     if len(v) > 1:
#         print(k, v)