from checker import check_candy
import random


def game_human(candy_full: int, candy_max: int, hum_count: int):
    if candy_full > 0:
        print(f"\nВсего осталось конфет: {candy_full}")
        if hum_count % 2 == 1:  # Ход игрока 1
            print("\nИгрок #1 делает ход")
            candy_full = candy_full - player_move(candy_full, candy_max)
            return game_human(candy_full, candy_max, hum_count + 1)
        else:  # Ход игрока 2
            print("\nИгрок #2 делает ход")
            candy_full = candy_full - player_move(candy_full, candy_max)
            return game_human(candy_full, candy_max, hum_count + 1)
    else:
        if hum_count % 2 == 0:
            print(f"\nПрошло {hum_count - 1} раундов.\nПобедил Игрок №1")
        else:
            print(f"\nПрошло {hum_count - 1} раундов.\nПобедил Игрок №2")


def player_move(candy_full: int, candy_max: int):
    hum_candy = int(input("Сколько возьмете конфет? "))
    if check_candy(hum_candy, candy_full, candy_max) is True:
        return hum_candy
    else:
        return player_move(candy_full, candy_max)


def game_bot(candy_full: int, candy_max: int, hum_count: int):
    if candy_full > 0:
        print(f"\nВсего осталось конфет: {candy_full}")
        if hum_count % 2 == 1:  # Ход игрока
            print("\nИгрок делает ход")
            candy_full = candy_full - player_move(candy_full, candy_max)
            return game_bot(candy_full, candy_max, hum_count + 1)
        else:  # Ход Bot
            if candy_full > candy_max:
                candy_full -= bot_move(candy_max)
                return game_bot(candy_full, candy_max, hum_count + 1)
            else:
                candy_full -= bot_move(candy_full)
                return game_bot(candy_full, candy_max, hum_count + 1)
    else:
        if hum_count % 2 == 0:
            print(f"\nПрошло {hum_count - 1} раундов.\nПобедил Игрок")
        else:
            print(f"\nПрошло {hum_count - 1} раундов.\nПобедил император И")


def bot_move(candy_max: int):
    bot_candy = random.randint(1, candy_max)
    print(f"\nБот делает ход: {bot_candy}")
    return bot_candy
