# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
import os
os.system('cls')                                        #Самоочистка терминала
n=int(input('Введите число: '))
k=int(input('Введите степень числа: '))
temp = 0
numbers = 1

while numbers <= k:
    numbers = n ** temp
    if numbers <= k:
        print (numbers, end = " ")
    temp += 1