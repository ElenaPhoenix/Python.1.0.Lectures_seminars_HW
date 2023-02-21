# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше 
# заданного максимума)
from random import randint
import os
os.system('cls')

array=[randint(1,20) for _ in range(int(input('Введите количество элементов массива: ')))]
print(array)
min_span=int(input('Введите диапазон чисел, минимальное значение: '))
max_span=int(input('Введите диапазон чисел, максимальное значение: '))

result=[]
for i in array:
    if i>=min_span and i<=max_span:
        result.append(i)
print(result)
