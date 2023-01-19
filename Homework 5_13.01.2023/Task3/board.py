def fill_board(board: list):
    print('_____________')
    for line in range(3):
        print('|', board[0 + line * 3], '|', board[1 + line * 3], '|', board[2 + line * 3], '|')
    print('_____________')
    # print(f"2 {game_board}")
    return board
