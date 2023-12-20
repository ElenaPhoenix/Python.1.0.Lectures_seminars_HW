# Множества - содержат в себе уникальные элементы (не повторяются), не обязательно упорядоченные
#Создание пустого множества:
q=set()
# colors={'red', 'green', 'blue'}
# print(type(colors))
# print(colors)
# colors.add('red')
# print(colors)                   # одинаковое значение второй раз не добавляется
# colors.add('gray')
# print(colors)
# colors.remove('red')            # удаление элемента. если попытаться удалить несуществующий элемент множества - будет ошибка
# print(colors)
# colors.discard('red')           # удаление элемента. если попытаться удалить несуществующий элемент - ошибки не будет
# print(colors)
# colors.clear()                  # удаление всех элементов множества
# print(colors)
# colors.update({'red':'red', 'green': 'green', 'blue': 'blue'})
# print(colors)


a={1, 2, 3, 5, 8}
b={2, 5, 8, 13, 21}
c=a.copy()                          # скопируется множество а
u=a.union(b)                        # объединятся множества a и b
i=a.intersection(b)                 # пересечение множеств a и b
dl=a.difference(b)                   # разность множества a и b
dr=b.difference(a)                   # разность множества b и a

q=a\
    .union(b)\
    .difference(a.intersection(b))


s=frozenset(a)                       # можно создать неизменяемые множества
