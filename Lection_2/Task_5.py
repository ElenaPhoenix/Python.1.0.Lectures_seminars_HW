# Словари - неупорядоченные коллекции произвольных объектов с доступом по ключу. Могут содержать разные типы данных
#Варианты создания словаря:
dictionary = {}
d=dict()
d["q"]='qwerty' #Ключу q соответствует значение qwerty
del d["q"] #Удаление элемента по ключу
print(d)

dictionary=\
    {
        'up': '^',
        'left': '<',
        'down': 'v',
        'right': '>'
    }
print(dictionary)
print(dictionary['left'])                # Типы ключей могут отличаться  

print(dictionary['up'])
dictionary['up']='upppp'                    # Можно присвоить новое значение переменной        
print(dictionary['up'])


for k in dictionary.keys():              # Можно получить все ключи/значения  
    print(k)

for k in dictionary.values():
    print(k)

for v in dictionary:                     # Можно пробежать по всем элементам словаря
    print(v)
    print(dictionary[v])

for (k, v) in dictionary.items():
    print (k, v)