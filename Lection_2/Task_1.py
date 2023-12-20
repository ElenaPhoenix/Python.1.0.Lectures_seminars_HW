# Файлы

# colors=['red', 'green', 'blue']
# data=open('file.txt', 'a')
# # data.writelines(colors)     # разделителей не будет
# data.write('\nLINE 2\n')
# data.write('LINE 3\n')
# data.close()                # после работы с файлом нужно его закрыть, в т.ч. чтобы не было утечки данных


# with open('file.txt', 'w') as data: #конструкция закрывает файл автоматически

#     data.write('LINE 1\n')
#     data.write('LINE 2\n')
# exit()                      # позволяет не выполнять ниже записанный код

path='file.txt'
data=open(path, 'r')
for line in data:
    print (line)
data.close()
exit()