# Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию, и Вы должны реализовать 
# функционал для изменения и удаления данных.

import os
os.system

def main_import_contacts():
    #with open(os.path.join(sys.path[0],'phonebook.txt'), 'r', encoding='utf-8') as data:
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        s=data.readlines()
        for i in range(len(s)):
            phonebook[i]=s[i].split()
        #print(phonebook)

def import_contacts(some_string):   #вывод из файла
    finded_contacts = list()
    for i in phonebook:
        if some_string in phonebook[i]:
            finded_contacts.append(phonebook[i])
    return finded_contacts

def export_contacts(new_cont): #запись в файл
    #with open(os.path.join(sys.path[0], 'phonebook.txt'), 'a+', encoding='utf-8') as data:
    with open('phonebook.txt', 'w') as data:
        s=' '.join(new_cont)
        data.writelines(' '.join(new_cont)+'\n')
        phonebook[len(phonebook)+1]=new_cont

def input_contact():
    new_contact=[input('surname: ')]
    new_contact.append(input('name: '))
    new_contact.append(input('given name: '))
    new_contact.append(input('phonenumber: '))
    #print(new_contact)
    export_contacts(new_contact)

def find_contact():
    s=import_contacts(input('wadda we search: '))
    print(*s)

def user_interface():
    main_import_contacts()
    print('Phonebook\nwhadda want?\n1 - add contact\n2 - find contact\n3 - print whole book\nany other input - end program')
    user_input=input('your choice: ')
    while user_input in ('1', '2', '3'):
        if user_input=='1':
            input_contact()
        elif user_input=='2':
            find_contact()
        elif user_input=='3':
            print()
            for i in phonebook:
                print(*phonebook[i])
        user_input=input('\nyour choice: ')
    print('bye')

phonebook=dict()

print(phonebook)
# input_contact()
# import_contacts()
# import_contacts('иванов')
user_interface()