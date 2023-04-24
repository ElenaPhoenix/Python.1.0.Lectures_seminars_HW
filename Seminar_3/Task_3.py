# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Примечание: Пользователь может вводить значения списка или список задан изначально.

# from random import randint              #вызвали randint из модуля random и используем его для работы как обычную функцию

# #my_list=[1, 2, 3, 4, 5]
# n=int(input("Введите количество чисел: "))
# my_list=[randint(1, 5) for i in range(n)]

# print(my_list)
# k=int(input("Введите число K: "))
# while k>0:                              #решение через цикл while
#     my_list.append(my_list[0])
#     my_list.remove(my_list[0])
#     k-=1
# print(my_list)
# for i in range(k):                      #решение через цикл for
#     my_list.append(my_list[0])
#     my_list.remove(my_list[0])
# print(my_list)


# my_list=[1,2,3,4,5]
# k=int(input())
# for i in range(k):
#     my_list.insert(0,my_list.pop())
# print(*my_list)

# Решения через срезы
your_list=[int(input('type element: ')) for i in range(int(input('type amount: ')))]
k=int(input('type K: '))%len(your_list)                                                 # % - чтобы счетчик дважды не проходил весь список, если длина меньше, чем сдвиг элементов 
print(your_list)
k_list=your_list[k:]+your_list[:k]
print(k_list)

# my_list=[1,2,3,4,5]
# k=int(input())
# print(*my_list[-k:],*my_list[:len(my_list)-k])