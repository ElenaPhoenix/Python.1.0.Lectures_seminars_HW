# 2 различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. 
# Программа получает на вход 1 натуральное число k, не превосходящее 105. Программа должна вывести все пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть выведена только 1 раз (перестановка чисел 
# новую пару не дает).

# k=int(input('Введите натуральное число: '))
# sum_dict=dict()
# for i in range(1,k+1):
#     sum_dict[i]=1
#     for j in range(2,(i//2)+1):
#         if i%j==0:
#             sum_dict[i]+=j

# for i in range(1, len(sum_dict)+1):
#     for j in range(i+1, len(sum_dict)+1):
#         if i==sum_dict[j] and j==sum_dict[i]:
#             print(i,j)


# Другой вариант решения
def sum_divided(n):
    div_sum=1
    for i in range(2,(n//2)+1):
        if n%i==0:
            div_sum+=i
    return div_sum

def friendly_pairs(x):
    div_list=[]
    for i in range(1,x+1):
        y=sum_divided(i)
        if y>i and sum_divided==i:
            div_list.append((i,y))
    return div_list

print(friendly_pairs(300))