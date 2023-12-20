# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах. Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем 
# пользователь вводит сами элементы множеств.

import os
os.system('cls')                                        #Самоочистка терминала

n={int(input('Введите поочередно с новой строки каждый элемент первого множества: ')) for i in range(int(input('Введите количество элементов первого множества: ')))}
m={int(input('Введите поочередно с новой строки каждый элемент второго множества: ')) for i in range(int(input('Введите количество элементов второго множества: ')))}
n&=m
print(n)
#print(type(n))                                  # set        
unique_list=list(set(n))
#print(type(unique_list))                        # list

temp=0
for i in range(len(unique_list)-1):
    if unique_list[i]>unique_list[i+1]:
        temp=unique_list[i]
        unique_list[i]=unique_list[i+1]
        unique_list[i+1]=temp

print(f'Неповторяемые числа из обоих множеств:', *unique_list)


# # Другой вариант решения
# from random import randint
# first_list=set(randint(1,20) for _ in range(int(input('Введите количество элементов первого множества: '))))
# print(first_list)
# second_list=set(randint(1,20) for _ in range(int(input('Введите количество элементов второго множества: '))))
# print(second_list)
# print('Пересекающиеся элементы: ')
# print(sorted(first_list.intersection(second_list)))


# # Другой вариант решения
# from random import randint
# first_list=int(input('Введите количество элементов первого множества: '))
# second_list=int(input('Введите количество элементов второго множества: '))

# list1=set[randint(1,20) for _ in range(first_list)]
# list2=set[randint(1,20) for _ in range(second_list)]

# list1_set=list(set(list1))
# list2_set=list(set(list2))
# print(list1_set,'<--list1   list2-->', list2_set)
# result=list(filter(lambda elem: elem in list1_set, list2_set))
# print(f'Общие элементы множеств: {result}')
