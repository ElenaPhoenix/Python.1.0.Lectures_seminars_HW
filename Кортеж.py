Создание кортежа(tuple)
a=(1,2,3,4)
a=1,2,3
a=tuple(range(12))
a=tuple([1,2,3,4,])
a=tuple((1,2,3,4,))
Операции как в списках
a=(1,2,3,4)*2=(1,2,3,4,1,2,3,4)
НЕизменяемый объект, но изменяемые объекты внутри картежа можно менять по прежнему
a.__sizeof__() - сколько байтов занимает картеж, словарь или список
sorted(my_tuple) - сортировка кортежа
*a - раскрывание итерируемого объекта
