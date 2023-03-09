# Написать EDA для датасета про пингвинов
# Необходимо:
# ● Использовать 2-3 точечных графика
# ● Применить доп измерение в точечных графиках, используя аргументы hue, size, stile
# ● Использовать PairGrid с типом графика на ваш выбор
# ● Изобразить Heatmap
# ● Использовать 2-3 гистограммы

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins")
penguins.head()

sns.scatterplot(data=penguins, x='island', y='flipper_length_mm')

sns.scatterplot(data=penguins, x='sex', y='flipper_length_mm')

sns.scatterplot(data=penguins, x='species', y='body_mass_g', hue='sex')

sns.histplot(data=penguins, x='species', y='bill_depth_mm', hue='sex')

sns.histplot(data=penguins, x='island', y='species', hue='sex')

cols=['body_mass_g', 'flipper_length_mm', 'bill_length_mm', 'bill_depth_mm']
g=sns.PairGrid(pg[cols])
g=map(sns.scatterplot)

sns.heatmap(pg.corr())

# Создать новый столбец в таблице с пингвинами, который будет отвечать за показатель длины клюва пингвина.
# high - длинный(от 42)
# middle - средний(от 35 до 42)
# low - маленький(до 35)

pg.loc[pg['bill_length_mm']>42, 'height_group']='high'
pg.loc[pg['bill_length_mm']>=35 & pg['bill_length_mm']<=42, 'height_group']='middle'
pg.loc[pg['bill_length_mm']<35, 'height_group']='low'
pg.head()


# Изобразить гистограмму по flipper_length_mm
# с оттенком height_group. Сделать анализ

sns.histplot(data=pg, x='flipper_length_mm', hue='height_group')