class Student:
    def __init__(self,name,student_id):
        self.name=name
        self.student_id=student_id
        self.grades=[]

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
        """Добавляет студентов в список, если он уже не там"""
        if student not in self.students:
            self.students.append(student)
        else:
            print('Студент уже числится у этого преподователя')

    def remove_student(self,student):
        """Убирает студентов из общего списка, если он есть в списке"""
        for student in self.students:
            if student in self.students:
                self.students.remove(student)
        else:
            print('Студент не числится  у этого преподователя')

    def list_students(self):
        """Выводит всех студентов преподователя"""
        print(f'\nСтуденты преподавателя {self.name} ({self.subject}):')
        for student in self.students:
            print(f'-{student.name} (ID: {student.student_id})')


if __name__=='__main__':
    teacher=Teacher('Ирина Сергеевна',35,'Английский язык')
    student1=Student('Иван Иванов',12345)
    student2=Student('John Smith',54764)

    teacher.add_student(student1)
    teacher.add_student(student2)
    teacher.list_students()

    print('\nСписок после удаления студента:')
    teacher.remove_student(12345)
    teacher.list_students()