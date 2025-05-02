import random

def blackjack():
    print('\n==Первая раздача==')
    cards_player=[random.randint(2,11),random.randint(2,11)]
    score_player=sum(cards_player)
    cards_dealer=[random.randint(2, 11)]
    score_dealer=sum(cards_dealer)
    print(f'Ваши карты: {cards_player}, ваши очки: {score_player}\nКарта дилера: {cards_dealer}, очки дилера: {score_dealer}')

    print('\n==Ваш ход==')
    while score_player<=21:
        choice=input('Вы хотите взять ещё карту? Введите "да" или "нет": ')
        if choice=='да':
            new_card=random.randint(2,11)
            cards_player.append(new_card)
            score_player+=new_card
            print(f'Выпала карта: {new_card}, ваши очки: {score_player}')
        elif choice=='нет':
            break
        else:
            print('Введите "да" или "нет"')

    if score_player>21:
        print('К сожалению, вы проиграли :(')
        play_again = input('\nХотите сыграть ещё раз?  Введите "да" или "нет": ')
        if play_again == 'да':
            return blackjack()
        elif play_again == 'нет':
            return
        else:
            print('Введите "да" или "нет"')

    print('\n==Ход дилера==')
    cards_dealer=[random.randint(2,11)]
    score_dealer=sum(cards_dealer)
    while score_dealer<17:
        new_card=random.randint(2,11)
        cards_dealer.append(new_card)
        score_dealer+=new_card
        print(f'Выпала карта: {new_card}, очки дилера: {score_dealer}')

    print('\n==Подведём итоги==')
    if score_dealer>21:
        print('У дилера больше 21 очка, поэтому вы победили!!')
    elif score_dealer==score_player:
        print('Ничья')
    elif score_player>score_dealer:
        print('Вы ближе к 21 очку, поэтому вы победили!!')
    else:
        print('К сожалению, вы проиграли :(')

    while True:
        play_again=input('\nХотите сыграть ещё раз? Введите "да" или "нет": ')
        if play_again=='да':
            return blackjack()
        elif play_again=='нет':
            return
        else:
            print('Введите "да" или "нет"')

if __name__=='__main__':
    blackjack()