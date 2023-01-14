def check_menu(num, num_lst):
    """
    Здесь проверяется что введены значения [1, 2, 3, 4, 9] или [1, 2] и только они
    """
    if len(num) == 1 and num.isdigit() is True and num in num_lst:
        return True
    else:
        print(f"\nВы ввели не корректное значение: {num} \n")
        return False


def check_candy(candy_hum: int, candy_full: int, candy_max: int):
    if 1 <= candy_hum <= candy_full and 1 <= candy_hum <= candy_max:
        return True
    else:
        print(f"\nВы ввели не корректное значение: {candy_hum} \n")
        return False
