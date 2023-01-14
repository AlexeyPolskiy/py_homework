"""
Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется
жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
a) Добавьте игру против бота
b) Подумайте как наделить бота ""интеллектом""
"""
from user_interface import main_menu
from game import game_human, game_bot


if __name__ == '__main__':
    candy_full = int(input('Введите количество конфет: '))
    candy_max = int(input('Введи максимальное количество конфет за ход: '))
    game = main_menu()
    if game == '9':
        print('\nИгры окончены')
    elif game == '1':
        game_human(candy_full, candy_max, 1)
    elif game == '2':
        game_bot(candy_full, candy_max, 1)


