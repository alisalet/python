import random
import datetime

def guess_number():
    number=random.randint(1, 101)
    number_attempts=0
    start=datetime.datetime.now()
    attempts=[]
    attempts.append(f'Начало игры: {start}')
    print('\nУгадай число от 1 до 100')

    while True:
        try:
            guess=int(input('Введите число: '))
            number_attempts+=1
            time_attempt=datetime.datetime.now()
            attempts.append(f'В {time_attempt} попытка №{number_attempts}: {guess}')
            if guess<number:
                print('Больше')
            elif guess>number:
                print('Меньше')
            else:
                print('Угадал! Молодец!!')
                finish=datetime.datetime.now()
                time_game=finish-start
                attempts.append(f'Число угадано в {finish}\nПонадобилось {number_attempts} попытки(-ок) и {time_game} времени')

                with open('log.txt','a',encoding='utf-8') as file:
                    file.writelines(f'{item}\n' for item in attempts)

                while True:
                    play_again=input('Хочешь сыграть ещё раз? Введите "да" или "нет": ')
                    if play_again=='да':
                        return guess_number()
                    elif play_again=='нет':
                        return
                    else:
                        print('Введите "да" или "нет"')

        except ValueError:
            print('Ошибка: вводите только числа')

if __name__=='__main__':
    guess_number()