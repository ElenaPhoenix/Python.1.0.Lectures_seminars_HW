# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – 
# количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
from random import randint
import os
os.system('cls')                                        #Самоочистка терминала

n=int(input('Введите количество элементов в массиве: '))
my_list=[randint(1, 10) for _ in range(n)]
print(my_list)
x=int(input('Введите искомое число: '))

counter=0

for i in range(0, len(my_list)):
    if my_list[i]==x:
        counter+=1
print('Число', x, 'встречается в массиве', counter, 'раз(а).')