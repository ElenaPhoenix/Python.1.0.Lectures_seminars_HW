# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше 
# заданного максимума)

from random import randint
import os
os.system('cls')

array=[randint(1,20) for _ in range(int(input('Введите количество элементов массива: ')))]
print(array)
min_span=int(input('Введите диапазон чисел, минимальное значение: '))
max_span=int(input('Введите диапазон чисел, максимальное значение: '))

for i in range(len(array)):
    if min_span<=array[i]<=max_span:
        print(i)


# Другой вариант решения:
# from random import randint

# def print_list_indexes(list0:list):
#     for i in range(len(list0)):
#         print(f'{i:3}', end=' ')
#     print()

# def print_list(list0:list):
#     for i in list0:
#         print(f'{i:3}', end=' ')
#     print()

# def range_list_indexes(list0:list, min0:int, max0:int):
#     range_list_indexes0 = []
#     for i in range(len(list0)):
#         if min0<=list0[i]<=max0:
#             range_list_indexes0.append(i)
#     return range_list_indexes0

# num=[randint(-10,10) for _ in range(20)]
# print_list_indexes(num)
# print_list(num)
# min_span=int(input('Введите диапазон чисел, минимальное значение: '))
# max_span=int(input('Введите диапазон чисел, максимальное значение: '))
# range_num_indexes=range_list_indexes(num,min_span,max_span)
# print('Индексы чисел, входящих в диапазон: ')
# print(range_num_indexes)


# Другой вариант решения:
# from random import randint
# start, stop=[int(i) for i in input('Enter range: ').split()]
# list_num=[randint(-10,10) for _ in range(randint(10,20))]
# print(list_num, [i for i, n in enumerate(list_num) if n in range(start,stop+1)], sep='\n')