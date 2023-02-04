#Дано натуральное число a>1. Определите, каким по счету числом Фибоначчи оно является, т.е. выведите такое число n, что ф(n)=a.
#Если а не является числом Фибоначчи, выведите число -1.
#Input: 5
#Output:6
import os
os.system('cls')                                        #Самоочистка терминала
a=int(input('Введите натуральное число '))
fib1=0
fib2=1
list=[0,1]
n=2
while a>fib2:
#    t=fib1
#    fib1=fib2
#    fib2=t+fib2
    fib1,fib2=fib2,fib1+fib2                            #Корректно работает при написании приравнивания в одну строку
    list.append(fib2)
    n+=1
print(f'Числа Фибоначчи \n {list}')
print(f'Число {a} по счету {n}-ое число Фибоначчи' if a==fib2 else f'Код -1: число {a} не является числом Фибоначчи')
