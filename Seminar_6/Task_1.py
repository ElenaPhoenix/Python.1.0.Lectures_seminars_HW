# Даны 2 массива чисел. Требуется вывести те элементы 1 массива (в том порядке, в каком они идут в 1 массиве), которых нет во 2 массиве. Пользователь 
# вводит число N - количество элементов в 1 массиве, затем N чисел - элементы массива. Затем число M - количество элементов во 2 массиве, затем 
# элементы 2 массива
from Seminar_6.module import creat_list
import os
os.system('cls')

n=int(input('Введите количество элементов 1 массива: '))
m=int(input('Введите количество элементов 2 массива: '))
n_list=creat_list(n)
m_list=creat_list(m)
z_list=[]
for i in range(n):
    if n_list[i] not in m_list:
        z_list.append(n_list[i])

print(*n_list)
print(*m_list)
print(*z_list)


# Другой вариант решения
# list1=[int(input(f'Введите {i+1}-е число:')) for i in range(int(input('Введите количество элементов 1 массива: ')))]
# list2=[int(input(f'Введите {j+1}-е число:')) for j in range(int(input('Введите количество элементов 2 массива: ')))]

# new_list=[el if el not in list2 else 0 for el in list1)]  #list complications: если появляется условие else, то ставим его перед for
# print(new_list)