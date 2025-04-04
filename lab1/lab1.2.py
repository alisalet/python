n=int(input('Введите число: '))
numbers=list(range(1, n+1))
for i in numbers:
    print(i)
for i in numbers:
    print(f'Квадрат {i}: {i**2}')
sum=0
for i in numbers:
    sum+=i
print(f'Сумма: {sum}')