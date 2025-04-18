class Student:
    def __init__(self,name,student_id):
        self.name=name
        self.student_id=student_id
        self.grades=[]

    def add_grade(self,grade):
        """Возвращает оценку с валидацией"""
        if 0<=grade<=10:
            self.grades.append(grade)
        else:
            print(f'Оценка {grade} недействительна')

    def get_average(self):
        """Возвращает средний балл"""
        return sum(self.grades)/len(self.grades) if self.grades else 0.0

    def display_info(self):
        """Всё красиво выводит"""
        print(f'Студент: {self.name}')
        print(f'ID: {self.student_id}')
        print(f'Оценки: {", ".join(map(str, self.grades))}')
        print(f'Средний балл: {self.get_average():.2f}\n')

    def __str__(self):
        """Возвращает всю информацию про студента в одной строчке"""
        return f'Студент {self.name} с ID {self.student_id} имеет средний балл {self.get_average():.2f}'

    def __eq__(self,other):
        """Возвращает совпадают ли ID студентов"""
        if isinstance(other,Student):
            return self.student_id==other.student_id
        return False

    def __len__(self):
        """Возвращает кол-во оценок"""
        return len(self.grades)

student1=Student('Иван Иванов', 12345)
student1.add_grade(3)
student1.add_grade(7.7)
student1.add_grade(10)
student1.add_grade(10)
student1.display_info()

student2=Student('fgcvigvy',00000)
student2.add_grade(11)
student2.add_grade(2)
student2.display_info()

student3=Student('Someone',12345)

print(student1)
print(f'student1==student2: {student1==student2}')
print(f'student1==student2: {student3==student2}')
print(f'{student1.name} имеет {len(student1)} оценки(-ок)')