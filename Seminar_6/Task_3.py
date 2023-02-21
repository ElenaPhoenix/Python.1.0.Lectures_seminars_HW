# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые 2 элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список чисел. Все числа списка находятся на разных строках.
# 1 1 1 1 - 2 пары

def find_pairs(numbers):
    count=0
    for i in range(1, len(arr)):
        if arr[i]==arr[i-1]:
            count+=1
    print(count)


arr=list(int(input(f'Enter {i+1} your num: ')) for i in range(int(input('Enter num len: '))))
print(arr)
arr.sort()
find_pairs(arr)


# Другой вариант решения 1 1 1 1 - 6 пар
# print('Введите элементы массива через пробел: ')
# list1=[int(i) for i in input().split()[:]]

# counter=0
# for i in list1:
#     for j in list1:
#         if i==j:
#             counter+=1
# print((counter-len(list1))//2)


# Другой вариант решения 1 1 1 1 - 6 пар
arr=[1, 1, 1, 1]
n=len(arr)
result=0

for i in range(n-1):
    for j in range(i+1, n):
        if arr[i]==arr[j]:
            result+=1
print(f'{arr} \n'
    f'Количество пар: {result}')
