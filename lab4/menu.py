from tictactoe import tictactoe
from random_number import guess_number
from blackjack import blackjack

def display_menu():
    print('\nВо что хотите поиграть?')
    print('1. Угадай число')
    print('2. Блэкджек (21 очко)')
    print('3. Крестики-нолики')
    print('0. Выход')

def main():
    while True:
        display_menu()
        choice=input('Выберите игру (0-3): ')

        if choice=='1':
            guess_number()
        elif choice=='2':
            blackjack()
        elif choice=='3':
            tictactoe()
        elif choice=='0':
            print('Спасибо за игру! Скорее возвращайтесь!!')
            break
        else:
            print('Введите цифру от 0 до 3')

if __name__=='__main__':
    main()