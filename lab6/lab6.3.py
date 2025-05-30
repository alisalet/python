import pandas as pd
students=pd.read_csv('students.csv')

print(f'Количество пропусков в таблице:\n{students.isnull().sum()}')

average_score=students['Score'].mean()
students['Score']=students['Score'].fillna(average_score)

students=students.dropna(subset=['Group'])

print(f'\nКоличество пропусков в таблице после обновления:\n{students.isnull().sum()}')
print(f'\nТаблица без пропусков:\n{students}')