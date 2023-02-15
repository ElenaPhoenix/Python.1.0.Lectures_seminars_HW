# Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).

from random import randint

def recurs(x):
    if x==0:
        print()
        return
    number=randint(0,21)
    print(number, end=" ")
    recurs(x-1)
    
    print(number, end=" ")

n=6
recurs(n)

