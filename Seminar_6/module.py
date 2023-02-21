def creat_list(n):          # создает лист из n элементов, вводимых пользователем
    coll=list(
        map(int,input(f'Введите через пробел {n} элементов: ').split()))
    
    if n>len(coll):
        return (f'Добавьте еще {n-len(coll)} элементов')
    elif n<len(coll):
        coll=(coll[:n])
    return coll
    