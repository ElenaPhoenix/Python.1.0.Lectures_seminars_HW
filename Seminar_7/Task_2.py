# Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь. Напишите 
# функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет ту, по которой вращается самая далекая планета. Круговые 
# орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет, зато искусственные спутники были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита представляет из себя кортеж из пары чисел - 
# полуосей ее эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса. При решении задачи используйте списочные 
# выражения. Подсказка: проще всего будет найти эллипс в 2 шага: сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс, имеющий 
# такую площадь. Гарантируется, что самая далекая планета одна.

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# one_lst, two_lst =zip(*orbits)
# my_list=[]
# for i in range (len(one_lst)):
#     if one_lst[i] == two_lst[i]:
#         my_list.append(0)
#     else:
#         s=one_lst[i]*two_lst[i]
#         my_list.append(s)
# for i in range (len(one_lst)):
#     if my_list[i] == max(my_list):
#         print(orbits[i])


# Другой вариант решения
# from math import pi

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# orbits=[i for i in orbits if i[0]!=i[1]]
# max_square=max([pi*i[0]*i[1] for i in orbits])
# max_square_a_b=[i for i in orbits if pi*i[0]*i[1]==max_square]
# print(max_square_a_b)


# Другой вариант решения
from math import pi

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
maximum=max(list(map(lambda x: pi*x[0]*x[1], (filter(lambda i: i[0]!=i[1], orbits)))))
far=filter(lambda y: pi*y[0]*y[1]==maximum, orbits)
print(*list(far))


# Другой вариант решения
# from functools import reduce
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# elliptic_orbits=list(filter(lambda x: x[0]!=x[1], orbits))
# print(reduce(lambda x,y: x if x[0]*x[1]>y[0]*y[1] else y, elliptic_orbits))
