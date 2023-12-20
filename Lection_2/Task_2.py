# Функции. Нужно по файлам распределять функционал. Из одного скрипта(файла) использовать функционал другого.
# Если в функции передаем какой-то аргумент, то он будет использоваться, если не передаем - будет использоваться аргумент по умолчанию(если это возможно)

# import Lection_1. Task_1. Hello_world as hello
# print(hello.f(1))


def new_string(symbol, count=3):
    return symbol * count
print(new_string('!', 5))           # !!!!!
print(new_string('!'))              # !!! - по умолчанию 3
print(new_string(4))                # 12 Python распознает тип данных в момент вызова функции

# Возможность передачи неограниченного количества аргументов. Для этого перед аргументом функции нужно поставить *(будет работа с аргументом как с набором).
def concatenatio(*params): # * позволяет передать неограниченное количество аргументов
    res: str = ''
    for item in params:
        res += item
    return res
print (concatenatio('a', 's', 'd', 'w'))    # asdw
print (concatenatio('a', '1'))              # a1
# print (concatenatio(1, 2, 3, 4))            # TypeError

