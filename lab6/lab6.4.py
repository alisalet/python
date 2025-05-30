import pandas as pd
students=pd.read_csv('students.csv')

students_by_group=students.groupby('Group')
for group_name,group_data in students_by_group:
    print(f'\nГруппа {group_name}:\n{group_data[["Name","Score"]]}')

average_score_groups=students_by_group['Score'].mean().round(2)
median_age=students_by_group['Age'].median()
print(f'\nСредний балл по группам:\n{average_score_groups}')
print(f'\nМедианный возраст по группам:\n{median_age}')

students['Passed']=students['Score'].apply(lambda x: 1 if x>=60 else 0)
print(f'\nТаблица со столбиком Passed:\n{students}')