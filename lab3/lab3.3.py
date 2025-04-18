from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self,height,width):
        self.height=height
        self.width=width

    def area(self):
        """Выводит площадь фигуры"""
        return self.height*self.width

    def perimeter(self):
        """Выводит периметр фигуры"""
        return (self.height+self.width)*2

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return math.pi*self.radius**2

    def perimeter(self):
        return 2*math.pi*self.radius

class Triangle(Shape):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def area(self):
        p=self.perimeter()/2
        return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))

    def perimeter(self):
        return self.a+self.b+self.c

def print_shape_info(shape):
    print(f'Площадь: {shape.area():.2f}')
    print(f'Периметр/Длина: {shape.perimeter():.2f}\n')

if __name__=='__main__':
    shapes=[Rectangle(12, 5),Circle(2),Triangle(3, 4, 5)]
    for shape in shapes:
        print_shape_info(shape)