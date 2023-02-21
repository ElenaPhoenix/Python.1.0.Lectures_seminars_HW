# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d. Каждое число вводится с новой строки.

import os
os.system('cls')

first_el=int(input('Введите первый элемент арифметической прогрессии: '))
step=int(input('Введите разность арифметической прогрессии (шаг): '))
quantity=int(input('Введите количество элементов арифметической прогрессии: '))

my_list=[]
for i in range(quantity):              #или в list complications: my_list=[first_el+(i-1)*step for i in range(1, quantity+1)]
    my_list.append(first_el)
    first_el+=step
print(*my_list)


# Другой вариант решения:
# a1 = int(input())
# d = int(input())
# n = int(input())
# for i in range(n):
# print(a1 + i * d)