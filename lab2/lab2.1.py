with open('data.txt') as file:
    #пробегаемся по строчкам в файле и добавляем значеня в пустой список, с которым будем работать
    numbers=[]
    for line in file:
        num = line.strip()
        if num:
            print(num)
            numbers.append(float(num))
sum=sum(numbers)
average=sum/len(numbers)
max=max(numbers)
min=min(numbers)
print(f"Сумма: {sum}")
print(f"Среднее: {average}")
print(f"Максимум: {max}")
print(f"Минимум: {min}")

with open('result.txt', 'w', encoding='utf-8') as file:
    file.write(f"Сумма: {sum}\n")
    file.write(f"Среднее: {average}\n")
    file.write(f"Максимум: {max}\n")
    file.write(f"Минимум: {min}\n")