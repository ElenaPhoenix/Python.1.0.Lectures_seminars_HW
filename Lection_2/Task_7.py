# Списки
#Способы задать список:
list_1=[]
list_1=list()
list_1=[1, 2, 3, 8]

list1=[1, 2, 3, 4, 5]
# list2=list1                                 # Можно копировать списки, но аккуратно
# for e in list1:
#     print(e)
# print()
# for e in list2:
#     print(e)
# print()

# list1[0]=123                                # Если меняем значение элемента в первом списке - меняется и во второй
# list2[1]=333                                # !!! Если меняем значение элемента во втором списке - меняется и в исходном!
# for e in list1:
#     print(e)
# print()
# for e in list2:
#     print(e)


print(list1)
print(len(list1))
print(list1.pop())                            # Удаление последнего элемента из списка
print(list1)

print(list1.pop(2))                           # Удаление конкретного элемента из списка
print(list1)

print(list1.insert(2, 11))                     # Добавление элемента в список. 2- индекс элемента, 11- значение
print(list1)

print(list1.append(555))                       # Добавление элемента в конец списка
print(list1)