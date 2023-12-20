# lambda function
# С одной переменной
def calc1(x):
    return x+10
print(calc1(10))

def calc2(x):
    return x*10
print(calc2(10))

def math(operat, x):            # В качестве аргумента operat может быть любая функция
    print(operat(x))

math(calc1, 10)
math(calc2, 10)


# С двумя переменными
def sum(x, y):
    return x+y

f=sum

sum1=lambda q,w: q+w              #Получится то же, что в def sum


def mylt(x, y):
    return x*y

def calc(operat, a, b):         # В качестве аргумента operat может быть любая функция
    print(operat(a, b))
    #return op(a, b) - второй вариант, вернуть значение

calc(mylt, 4 , 5)
calc(f, 4, 5)                   # f - переназвали функцию, можно также свободно пользоваться  
calc(sum1, 4, 5)

# Можно не создавать функцию sum1, а сразу сделать действия с lambda:
calc(lambda q,w: q+w, 4, 5)

    


