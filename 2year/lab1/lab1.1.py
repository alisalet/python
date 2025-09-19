class Student:
    def __init__(self,name,group,grades):
        self.name=name
        self.group=group
        self.grades=grades

    def average_grade(self):
        average=sum(self.grades)/len(self.grades)
        return average if self.grades else 0.0

    def is_excellent(self):
        return self.average_grade()>=4.5

students=[]
with open('students.txt', encoding='utf-8') as file:
    for line in file:
        line=line.strip()
        if line:
            parts=line.split(';')
            if len(parts)>=3:
                name=parts[0].strip()
                group=int(parts[1].strip())
                grades_str=parts[2].strip()
                grades=[int(grade.strip()) for grade in grades_str.split(',')]
                student=Student(name,group,grades)
                students.append(student)

excellent_students=[student for student in students if student.is_excellent()]
with open('excellent_students.txt', 'w', encoding='utf-8') as file:
    for student in excellent_students:
        file.write(f'{student.name} - {student.group}\n')

group_average={}
for student in students:
    if student.group not in group_average:
        group_average[student.group]=[]
    group_average[student.group].append(student.average_grade())

print('Средний балл для каждой группы:')
for group,average in sorted(group_average.items()):
    avrg=sum(average)/len(average) if average else 0
    print(f'Группа №{group}: {avrg:.2f}')
print(f'Найдено {len(excellent_students)} отличников')