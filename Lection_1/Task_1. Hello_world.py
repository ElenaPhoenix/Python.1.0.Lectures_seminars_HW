#print ('hello world')

#value=None
#print(type(value))
#a=123
#b=1.23
#print(type(a))
#print(type(b))
#value=345
#print(type(value))
#s='hello \nworld'
#print(s) #вывод строки
#print(a,b,s)
#print(a, '-',b, '-',s)
#print('{1} - {2} - {0}'.format(a, b, s)) # можно менять местами с помощью индексов
#print(f'{a} - {b} - {s}')
#f=False
#print(f)

#list=['1', '2', '3'] #можно создать пустой массив list=[]
#col=['hello', 1, 2, 4.5, True]
#print(list)

#print('Введите a');
#a=int(input())
#print('Введите b');
#b=int(input())
#print(a, ' + ', b, ' = ', a+b)
#print('{}{}'.format(a,b))
#print(f'{a} {b}')

#f=[1,2,3,4]
#print(f)
#print(not 2 in f)

#is_odd=not f[0]%2 #по умолчанию в Python 0 - ложь, 1 - истина
#print(is_odd)


#Управляющие конструкции if, if-else
#a=int(input('a = '))
#b=int(input('b = '))
#if a>b:
#    print(a)
#else:
#    print(b)


#Конструкция elif
#username=input('Введите имя: ')
#if username=='Лена':
#    print('Ура, это же ЛЕНА!')
#elif username == 'Ирина':
#    print('Я так ждала Вас, Ирина')
#elif username=='Елена':
#    print('Елена - топ ;)')
#else:
#    print('Привет,', username)


#Управляющая конструкция while
#original=23
#inverted=0
#while original!=0:
#    inverted=inverted*10+(original%10)
#    original//=10
#print(inverted)


#Управляющая конструкция while-else
#original=23
#inverted=0
#while original!=0:
#    inverted=inverted*10+(original%10)
#    original//=10
#    print(original)
#else:
#    print('Пожалуй')
#    print('хватит')
#print(inverted)


#Управляющая конструкция for
#for i in 1,2,3,4,5:
#    print(i**2)

#list=[1,2,3,4,10,5]
#for i in list:
#    print(i)

#r=range(10)
#for i in r:
#    print(i)

#for i in range(5):
#    print(i)

#for i in range(1,7):
#    print(i)

#for i in range(1,10,2):
#    print(i)

#for i in 'qwe - rty':
#    print(i)


#Строки
#text='съешь еще этих мягких французских булок'
#print(len(text))
#print('еще' in text)
#print(text.isdigit())
#print(text.islower())
#print(text.replace('булок', 'БУЛОК'))


#Строки. Срезы
#text='съешь еще этих мягких французских булок'
#print(text[0])
#print(text[1])
#print(text[len(text)-1])
#print(text[-5])
#print(text[:])  #по умолчанию это print(text[0:len(text)-1]), то есть распечатает весь текст от нулевого до последнего символа
#print(text[:2])
#print(text[len(text)-2:])
#print(text[2:9])
#print(text[6:-18])
#print(text[0:len(text):6])
#print(text[::6])
#text=text[2:9]+text[-5]+text[:2]


#Списки
#numbers=[1, 2, 3, 4, 5]
#print(numbers)
#ran=range(1,6)
#numbers=list(ran) #приведение типа range к типу list
#print(numbers)
#numbers[0]=10
#print(f'{len(numbers)} len')
#print(numbers)
#for i in numbers:
#    i*=2        #кладется новое значение в переменную, не в сам список, список остается без изменений
#    print(i)
#print(numbers)

#colors=['red', 'green', 'blue']
#for e in colors:
#    print(e)

#for e in colors:
#    print(e*2)

#colors.append('gray') #добавить в конец
#print(colors==['red', 'green', 'blue', 'gray'])
#colors.remove('red') #удалить элемент, можно также использовать del colors[0]
#print(colors)


#Функции def function_name(x):
def f(x):
    if x==1:
        return 'Целое'
    elif x==2.3:
        return 23
    else:
        return
arg=1
print(f(arg))


