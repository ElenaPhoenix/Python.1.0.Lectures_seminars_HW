# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# s='a a a b c a a d c d d'
# s=s.split()
# print(s)
# result_dict={}                          # создаем словарь, в который будем класть счетчики какой символ сколько раз встречается
# new_s=[]                                # создаем лист, в который будем класть по условию к задаче
# for i in s:
#     if i not in result_dict:            # если еще нет в словаре, в первый раз
#         new_s.append(i)                 # кладем символ в новый список
#         result_dict[i]=result_dict.get(i,0)+1   # с помощью метода get возвращаем в словарь наш символ искусственно  
#     else:                                   # если уже есть в словаре, значит, пошли повторы
#       new_s.append(f'{i}_{result_dict[i]}')
#       result_dict[i]=result_dict.get(i,0)+1
# print(*new_s)                           # распаковываем лист


#Другой вариант решения
# text='a a a b c a a d c d d'
# text=text.split()
# print(text)
# result=''
# d={}
# for i in range(len(text)):
#     if text[i] not in d:
#         d[text[i]]=1
#         result+=f'{text[i]}'
#     else:
#         result+=f'{text[i]}_{d[text[i]]}'
#         d[text[i]]+=1

# print(result)


#Другой вариант решения
s='a a a b c a a d c d d'
s=s.split()
print(s)
my_dict=dict()
for i in set(s):
    my_dict[i]=-1
for i in s:
    my_dict[i]+=1
    if my_dict[i]==0:
        print(i, end=' ')
    else: print(i, end=f'_{my_dict[i]} ')  