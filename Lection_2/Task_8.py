#List comprehension - генератора списка
#Варианты использования:
# list_1 = [exp for item in iterable]
# list_1 = [exp for item in iterable (if conditional)]

list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]
list_1 = [i for i in range(1, 101) if i % 2 == 0] # [2, 4, 6,..., 100]
list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0] # [(2, 2), (4, 4),..., (100, 100)]
list_1 = [i * 2 for i in range(10) if i % 2 == 0]
print(list_1) # [0, 4, 8, 12, 16]