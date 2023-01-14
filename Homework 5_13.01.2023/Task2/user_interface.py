from checker import check_menu


def main_menu():
    print("\nС кем Вы будете играть?\n"
          "1. С человеком\n"
          "2. С ботом\n"
          "9. Выключить\n")
    num_menu = input(f"Введите номер необходимого действия ==> ")
    num_lst = ['1', '2', '9']
    if check_menu(num_menu, num_lst) is True:
        return num_menu
    else:
        main_menu()



