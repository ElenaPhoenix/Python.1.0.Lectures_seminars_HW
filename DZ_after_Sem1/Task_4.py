#Определить, можно ли от шоколадки размером n x m долек отломить k долек, если разрешается сделать 1 разлом по прямой между дольками, т.е. разломить шоколадку на 2 прямоугольника
import os
os.system('cls')                                        #Самоочистка терминала
n=int(input('Введите длину шоколадки: '))
m=int(input('Введите ширину шоколадки: '))
k=int(input('Введите количество долек шоколадки: '))
if k <= m*n and (k%m==0 or k%n==0):
    print('Да, можно отломить', k, 'долек')
else:
    print('Нет, нельзя отломить', k, 'долек')