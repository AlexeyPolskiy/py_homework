from checker import check_input
from checker import check_board


def move_input(board: list, player_token: str):
    while True:
        value = input(f'Куда поставить {player_token} ? ==> ')
        if check_input(value, '123456789') is False:
            continue
        else:
            value = int(value)
            if check_board(value, board) is False:
                continue
            else:
                board[value - 1] = player_token
                # print(f"2 {game_board}")
                return board
            break
