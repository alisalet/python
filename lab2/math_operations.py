def add(a,b):
    print(a+b)

def substract(a,b):
    print(a-b)

def multiply(a,b):
    print(a*b)

def divide(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print('Ошибка: нельзя делить на ноль')