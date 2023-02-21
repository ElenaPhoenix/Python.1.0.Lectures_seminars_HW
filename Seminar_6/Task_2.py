# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов, у которых оба соседних элемента 
# меньше данного. Сначала вводится число N — количество элементов в массиве. Далее записаны N чисел — элементы массива. 

# from Seminar_6.module import creat_list
# import os
# os.system('cls')

# n=int(input('Введите количество элементов массива: '))
# num_list=creat_list(n)
# print(num_list)
# test_trio=[]
# count=0
# for i in range(len(num_list)-2):
#     test_trio=num_list[i:i+3]
#     if test_trio[1]==max(test_trio):            #или так: if test_trio[0]<if test_trio[1]>if test_trio[2]
#         count+=1
# print(count)


# Другой вариант решения
from random import randint
array=[randint(1,10) for _ in range(int(input('Введите количество элементов массива: ')))]
print(array)
# count=0
# for i in range(1, len(array)-1):
#     if array[i]>array[i-1] and array[i]>array[i+1]:
#         count+=1
# print(count)

res_array=[1 for i in range(1, len(array)-1) if array[i-1]<array[i]>array[i+1]]
print(len(res_array))