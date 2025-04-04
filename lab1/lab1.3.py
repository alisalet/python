n=int(input('Введите число: '))
f=1
while n>0:
    print(n)
    f*=n
    n-=1
print(f'Факториал: {f}')