"""
Создайте программу для игры в ""Крестики-нолики"".
"""

import emoji
# print(emoji.emojize('Python is :thumbs_up:'))
# print(emoji.emojize('Python is :cross_mark:'))
# print(emoji.emojize('Python is :hollow_red_circle:'))

# emoji.emojize(":hollow_red_circle:")
# emoji.emojize(":cross_mark:")


# Инициализация карты
maps = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]

# print(type(maps))

# Инициализация победных линий
victories = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]

# print(type(victories))

# Вывод карты на экран
def print_maps():
    print(maps[0], end=" ")
    print(maps[1], end=" ")
    print(maps[2])

    print(maps[3], end=" ")
    print(maps[4], end=" ")
    print(maps[5])

    print(maps[6], end=" ")
    print(maps[7], end=" ")
    print(maps[8])

# Сделать ход в ячейку
def step_maps(step,symbol):
    ind = maps.index(step)
    maps[ind] = symbol


# Получить текущий результат игры
def get_result():
    win_player = ""

    for i in victories:
        if maps[i[0]] == emoji.emojize(":cross_mark:") and maps[i[1]] == emoji.emojize(":cross_mark:") and \
                maps[i[2]] == emoji.emojize(":cross_mark:"):
            win_player = emoji.emojize(":cross_mark:")
        if maps[i[0]] == emoji.emojize(":hollow_red_circle:") and maps[i[1]] == emoji.emojize(":hollow_red_circle:") \
                and maps[i[2]] == emoji.emojize(":hollow_red_circle:"):
            win_player = emoji.emojize(":hollow_red_circle:")

    return win_player


# Основная программа
game_over = False
player1 = True

while not game_over:

    # 1. Показываем карту
    print_maps()

    # 2. Спросим у играющего куда делать ход
    if player1:
        symbol = emoji.emojize(":cross_mark:")
        step = int(input("Человек 1, ваш ход: "))
    else:
        symbol = emoji.emojize(":hollow_red_circle:")
        step = int(input("Человек 2, ваш ход: "))

    step_maps(step, symbol)  # делаем ход в указанную ячейку
    win = get_result()  # определим победителя
    if win != "":
        game_over = True
    else:
        game_over = False

    player1 = not player1

# Игра окончена. Покажем карту. Объявим победителя.
print_maps()
print("Победили", win)
