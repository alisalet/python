import random
numbers=[random.randint(1, 101) for i in range(20)]
print(numbers)
even_numbers=list(filter(lambda x:x%2==0,numbers))
print(f'Чётные: {even_numbers}')
devided_by_3=list(filter(lambda x:x%3==0,numbers))
print(f'Делятся на 3: {devided_by_3}')
print(f'Среднее: {sum(numbers)/20}')