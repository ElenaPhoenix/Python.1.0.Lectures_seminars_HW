# 1. Изобразите отношение households к population с помощью точечного графика
# 2. Визуализировать longitude по отношения к median_house_value, используя линейный график
# 3. Представить гистограмму по housing_median_age
# 4. Изобразить гистограмму по median_house_value с оттенком housing_median_age

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('Seminar_10\california_housing_train.csv')
sns.scatterplot(data=df, x='households', y='population')

sns.relplot(x='longitude', y='median_house_value', kind='line', data=df, height=10, aspect=2)

sns.relplot(y='longitude', x='median_house_value', kind='line', data=df, height=10, aspect=2)
df.columns

plt.figure(figsize=(30,17))
sns.histplot(data=df, x='median_house_value', hue='housing_median_age')
