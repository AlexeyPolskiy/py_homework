def check_input(num: str, num_str: str):
    """
    Здесь проверяется что введены значения 1, 2, 3, 4, 5, 6, 7, 8, 9
    """
    if len(num) == 1 and num in num_str:
        return True
    else:
        print(f"\nВы ввели не корректное значение: {num} \n")
        return False


def check_board(value: int, board: list):
    if str(board[value - 1]) in 'XO':
        print('Эта клетка уже занята')
        return False
    else:
        return True


def check_win(win_line: list, board):
    for field in win_line:
        if (board[field[0] - 1]) == (board[field[1] - 1]) == (board[field[2] - 1]):
            return board[field[1] - 1]
    else:
        return False
