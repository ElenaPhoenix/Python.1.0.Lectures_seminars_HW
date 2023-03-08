import pandas as pd
df=pd.read_csv(Seminar_9/california_housing_train.csv)

df.shape

df.dtypes

# 1. Проверить есть ли в файле пустые значения
# 2. Показать median_house_value где median_income < 2
# 3. Показать данные в первых 2 столбцах
# 4. Выбрать данные где housing_median_age < 20 и
# median_house_value > 70000
df.isnull().sum()
df[df['median_income']<2]['median_house_value','median_income']
df.iloc[:,[0,1]]
df[(df['housing_median_age']<20) & (df['median_house_value']>70000)]

# 1. Определить какое максимальное и минимальное
# значение median_house_value
# 2. Показать максимальное median_house_value, где
# median_income = 3.1250
# 3. Узнать какая максимальная population в зоне
# минимального значения median_house_value
max(df['median_house_value'])
min(df['median_house_value'])
df[df['median_income']==3.125]['median_house_value'].max()
df[df['median_house_value']==df['median_house_value'].min()]['population'].max()

df2[(df['median_house_value']==df['median_house_value'].min())]
df2[df2['population']==df2['population'].max()]
