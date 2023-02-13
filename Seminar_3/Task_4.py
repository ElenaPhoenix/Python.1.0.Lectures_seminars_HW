# Напишите программу для печати всех уникальных значений в словаре.
# Примечание: Список словарей задан изначально (на выходе - множество). Пользователь его не вводит

# my_list=[{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
#         {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
# list1=[]
# for i in my_list:
#     for value in i.values():
#         list1.append(value)
# print(set(list1))

#Другой вариант решения
def unic_values(lst):
    unic_values=set()
    for d in lst:
        for value in d.values():
            unic_values.add(value.strip())                          # Избавляемся от пробелов и переносов строк 
    return unic_values
input_list=[{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
print(unic_values(input_list))
