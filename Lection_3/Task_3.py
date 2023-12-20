def select(func, collect):
    return [func(x) for x in collect]

def where(func, collect):
    return [x for x in collect if func(x)]

data='1 2 3 5 8 15 23 38'.split()
print(data)
res=select(int, data)           # преобразовали список строк в список чисел
print(res)

res=where(lambda x: not x%2, res)
print(res)

res=select(lambda x:(x, x**2), res)
print(res)

# Есть аналог - функция map. map() - применяет указанную функцию к каждому элементу итерируемого объекта и возвращает итератор с новыми объектами 
my_list=[x for x in range(1, 21)]
my_list=list(map(lambda x: x+10, my_list))
print(my_list)


data=list(map(int, input('Введите числа через пробел: ').split()))
print(data)

#можно не приводить в list.  но тогда введенные данные можно будет использовать только 1 раз, они нигде не сохранятся. Сохранить можно в list
data1=map(int, input('Введите числа через пробел: ').split())
for e in data1:
    print(e*10)
print('xyz')
for e in data1:
    print(e*10)


# Преобразуем первый пример с map():
def where(func, collect):
    return [x for x in collect if func(x)]

data='1 2 3 5 8 15 23 38'.split()
print(data)
res=map(int, data)           # преобразовали список строк в список чисел
print(res)

res=where(lambda x: not x%2, res)
print(res)

res=list(map(lambda x:(x, x**2), res))
print(res)