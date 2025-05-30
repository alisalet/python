import pandas as pd
students=pd.read_csv('students.csv')

highscore=students[students['Score']>80]
highscore_sort=highscore.sort_values('Score',ascending=False)
print(f'Студенты с баллом выше 80 по убыванию:\n{highscore_sort}')
oldest_student=students.loc[students['Age'].idxmax()]
youngest_student=students.loc[students['Age'].idxmin()]
print(f'\nСамый старший студент:\n{oldest_student}')
print(f'\nСамый младший студент:\n{youngest_student}')