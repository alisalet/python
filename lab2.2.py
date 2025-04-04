try:
    x=float(input('Введите первое число: '))
    y=float(input('Введите второе число: '))
    print(x/y)
except ZeroDivisionError:
    print('Ошибка: нельзя делить на ноль')
except ValueError:
    print('Ошибка: вводите только числа')