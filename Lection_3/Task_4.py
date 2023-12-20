#Вместо функции where есть функция filter() - применяет указанную функцию к каждому элементу итерируемого объекта и возвращает итератор с теми объектами, для которых функция вернула True.
data=[x for x in range(10)]
res=(filter(lambda x: x%2==0,data))
print(res)

# Преобразуем в list:
res1=list(filter(lambda x: x%2==0,data))    #запись на python: res1=list(filter(lambda x: not x%2,data))
print(res1)

ex_data='1 2 3 5 8 15 23 38'.split()
print(ex_data)
ex_res=list(filter(lambda x: not x%2, res))
print(ex_res)