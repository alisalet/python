def gameboard(board):
    for i in range(3):
        print(f' {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} ')
        if i<2:
            print("-----------")

def check_winner(board):
    win_lines=[
        [0,1,2],[3,4,5],[6,7,8],#строчки
        [0,3,6],[1,4,7],[2,5,8],#столбики
        [0,4,8],[2,4,6] #диагонали
    ]
    for line in win_lines:
        if board[line[0]]==board[line[1]]==board[line[2]]!=' ':
            return board[line[0]]
    return 'Ничья' if ' ' not in board else None

def tictactoe():
    board=[' ']*9
    current_player='X'
    print('Выбери, куда сделать ход (в клетку под номером от 1 до 9):')
    print('1 | 2 | 3')
    print('4 | 5 | 6')
    print('7 | 8 | 9')

    while True:
        gameboard(board)
        move=input(f'Ход игрока {current_player}: ')
        try:
            move=int(move)-1
            if move<0 or move>8:
                print('Введите число от 1 до 9!')
                continue

            if board[move]!=' ':
                print('Клетка занята!')
                continue

            board[move]=current_player
            winner=check_winner(board)

            if winner:
                gameboard(board)
                if winner=='Ничья':
                    print('Ничья')
                else:
                    print(f'Игрок {winner} победил')
                break

            current_player='O' if current_player=='X' else 'X'

        except ValueError:
            print('Введите число от 1 до 9!')

    while True:
        play_again = input('\nХочешь сыграть ещё раз? Введите "да" или "нет": ')
        if play_again == 'да':
            return tictactoe()
        elif play_again == 'нет':
            return
        else:
            print('Введите "да" или "нет"')

if __name__=='__main__':
    tictactoe()