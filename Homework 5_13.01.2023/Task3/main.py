"""
Создайте программу для игры в ""Крестики-нолики"".
"""
from board import fill_board
from move import move_input
from checker import check_win


if __name__ == '__main__':
    victorious_line = [(1, 2, 3),
                       (4, 5, 6),
                       (7, 8, 9),
                       (1, 4, 7),
                       (2, 5, 8),
                       (3, 6, 9),
                       (1, 5, 9),
                       (3, 5, 7)]
    count = 0
    board = list(range(1, 10))
    while True:
        game_board = fill_board(board)
        # print(f"1 {game_board}")
        if count % 2 == 0:
            move_input(game_board, 'X')
        else:
            move_input(game_board, 'O')
        if count > 3:
            win = check_win(victorious_line, game_board)
            if win:
                game_board = fill_board(board)
                print(win, 'выиграл!')
                # print(f"{count}")
                break
        count += 1
        if count > 8:
            game_board = fill_board()
            print('Ничья!')
            break
