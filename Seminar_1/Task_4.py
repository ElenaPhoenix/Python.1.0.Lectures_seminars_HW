#Дано натуральное число. Требуется определить, является ли год с данным номером высокосным. Если год является высокосным, то выведите
#YES, иначе выведите NO.(Год является высокосным, если его номер кратен 4 или 400, но не кратен 100 )
#Input:2016
#Output:YES
import os
os.system('cls')                                        #Самоочистка терминала
def num_input(invite_msg):                              #Функция проверки ввода значений
    user_input=input(invite_msg)
    try:
        return(int(user_input))
    except:
        print('Нужно ввести целое число. Попытайтесь снова')
        return num_input(invite_msg)

year=input('Введите номер года: ')
if year%400==0 or year%100!=0 and year %4==0:
    print('YES')
else:
    print('NO')