# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки 
# были повернуты вверх одной и той же стороной. Выведите минимальное количество монет,
# которые нужно перевернуть.
import os
os.system('cls')                                        #Самоочистка терминала
import random
n=int(input('Введите количество монет: '))
list1=[]

for i in range(n):
    list1.append(random.randint(0,1))
print(list1)

count=0
min_count=0
for temp in list1:
    if temp==0:
        count+=1
    elif temp==1:
        min_count+=1
if count<min_count:
    min_count=count
print(f'Нужно перевернуть минимум {min_count} монет')