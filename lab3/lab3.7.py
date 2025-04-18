class Student:
    def __init__(self,name,student_id):
        self.name=name
        self.student_id=student_id
        self.grades=[]

    def add_grade(self,grade):
        if 0<=grade<=10:
            self.grades.append(grade)
        else:
            print(f'Оценка {grade} недействительна')

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Teacher(Person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject=subject
        self.students=[]

    def add_student(self,student):
        if isinstance(student,Student):
            self.students.append(student)
        else:
            print('Можно добавлять только объекты класса Student')

    def remove_student(self, student_id):
        self.students=[s for s in self.students if s.student_id != student_id]

class Assistant(Student,Teacher):
    def __init__(self,name,student_id,age,subject):
        Student.__init__(self,name,student_id)
        Teacher.__init__(self,name,age,subject)

    def help_student(self,student):
        """Выводит информауию о помощи ассистента студенту"""
        print(f'{self.name} помогает студенту по имени {student.name} с предметом {self.subject}')

if __name__=='__main__':
    a=Assistant('Вася',65743,20,'Программирование')
    s=Student('Иван',12345)

#Работа методов
    a.add_grade(9)
    a.add_student(s)
    a.help_student(s)