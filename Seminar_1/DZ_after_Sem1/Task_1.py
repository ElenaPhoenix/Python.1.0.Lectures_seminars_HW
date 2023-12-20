#Найдите сумму цифр трехзначного числа
import os
os.system('cls')                                        #Самоочистка терминала

number=input('Введите трехзначное число: ')
digit_1= int(number[0])
digit_2 = int(number[1])
digit_3 = int(number[2])
print("Сумма цифр числа = ", digit_1 + digit_2 + digit_3)
