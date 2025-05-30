import matplotlib.pyplot as plt
import pandas as pd
students=pd.read_csv('students.csv')

students['Score'].hist(bins=20,color='#40a6e6',edgecolor='#3c7ee8')
plt.title('Распределение баллов')
plt.xlabel('Баллы')
plt.ylabel('Количество студентов')
plt.grid(False)
plt.show()

students_by_group=students.groupby('Group')
average_score_groups=students_by_group['Score'].mean().round(2)
average_score_groups.plot(kind='bar',color=['#f060c9','#b66ef5','#40a6e6'])
plt.title('Средний балл по группам')
plt.xlabel('Группы')
plt.ylabel('Баллы')
plt.xticks(rotation=0)
plt.ylim(0,100)
plt.show()
