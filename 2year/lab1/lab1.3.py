import pandas as pd
import matplotlib.pyplot as plt

dataframe={'Товар': ['Twix','KitKat','Snickers','Mars','MilkyWay','Bounty'],
           'Цена': [75,100,80,None,50,65],
           'Количество': [10,15,6,100000,-3,5]}
df=pd.DataFrame(dataframe)
print(f'Изначальная таблица:\n{df}\n')
df['Цена']=df['Цена'].fillna(df['Цена'].median())
print(f'Таблица без пропусков в цене:\n{df}\n')
df=df[(df['Количество']>=1)&(df['Количество']<=1000)]
print(f'Таблица без строчек, где кол-во является выбросом:\n{df}\n')
df['Общая стоимость']=df[('Цена')]*df['Количество']
print(f'Появился новый столбец:\n{df}\n')
income=df.groupby('Товар')['Общая стоимость'].sum()
print(f'Доход по каждому товару:\n{income}\n')

plt.bar(income.index, income.values, color='#b66ef5')
plt.title('Доход по товарам')
plt.xlabel('Товар')
plt.ylabel('Доход')
plt.show()