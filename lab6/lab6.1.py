import pandas as pd

students=pd.read_csv('students.csv')

print(f'Первые 5 строк:\n{students.head()}')
print('\nИнформация о данных:')
print(students.info())
print(f'\nСтатистика:\n{students.describe()}')
average_score=students['Score'].mean()
student_groups=students['Group'].value_counts()
print(f'\nСредний балл студентов: {average_score:.2f}')
print(f'\nКоличество студентов в каждой группе: {student_groups}')