# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – 
# количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
from random import randint
import os
os.system('cls')                                        #Самоочистка терминала

n=int(input('Введите количество элементов в массиве: '))
my_list=[randint(1, 20) for _ in range(n)]
print(my_list)
x=int(input('Введите натуральное число: '))

my_list.sort()
print('Упорядоченный список:', my_list)

nearest_number=0
for i in range(0, len(my_list)-1):
    if my_list[i]==x:
        nearest_number=my_list[i]
        break
    elif abs(my_list[i]-x)<=abs(my_list[i+1]-x):
        nearest_number=my_list[i]
        break
print('В массиве ближайшим к заданному является число:', nearest_number)
