x=int(input('Введите первое число: '))
y=int(input('Введите второе число: '))
z=int(input('Введите третье число: '))
print(f'Максимальное: {max(x,y,z)}')
print(f'Минимальное: {min(x,y,z)}')
if x==y==z:
    print("Все числа равны")
else:
    print("Числа не равны")