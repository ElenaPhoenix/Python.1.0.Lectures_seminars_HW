import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

# создаем новые столбцы, присваиваем им значение False
data = pd.DataFrame().assign(robot=False, human=False)

# функция, которую будем применять к каждому элементу столбца 'whoAmI'
def set_one_hot(row):
    if row['whoAmI'] == 'robot':
        row['robot'] = True
    elif row['whoAmI'] == 'human':
        row['human'] = True
    return row

# применяем функцию set_one_hot() к каждой строке в столбце 'whoAmI'
data = data.assign(whoAmI=lst).apply(set_one_hot, axis=1)

# удаляем исходный столбец 'whoAmI'
data = data.drop(columns=['whoAmI'])

print(data.head())