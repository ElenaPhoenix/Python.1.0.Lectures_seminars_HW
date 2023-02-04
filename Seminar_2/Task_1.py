#По данному целому неотрицательному n вычислите значение n!. n!=1*2*3*...*n (произведение всех чисел от 1 до n). 0!=1. Решить задачу, используя цикл while
#Input: 5
#Output:120
import os
os.system('cls')                                        #Самоочистка терминала
n=int(input('Введите целое неотрицательное число: '))
def Factorial(number):
    factorial=1
    i=1
    while i<=n:
        factorial*=i
        i+=1
    return factorial

while n<0:
    print('Введено число меньше 0, введите другое число')
    n=int(input('Введите целое неотрицательное число: '))
else:
    Factorial_n=Factorial(n)
    print(Factorial_n)


#Другой вариант решения
#n=int(input('Введите целое неотрицательное число: '))
#factorial=1
#while n>1:
#    factorial*=n
#    n-=1
#print(factorial)
