from checker import check_menu
from changes_directory import view_entry, add_entry


def menu():
    print("Меню справочника. \n"
          "1 - Просмотр записей справочника \n"
          "2 - Добавление записи в справочник \n"
          "3 - Экспорт справочника \n"
          "4 - Импорт справочника \n"
          "9 - Выход \n")
    lst_num = ['1', '2', '3', '4', '9']
    num_menu = input(f'Введите номер необходимого действия ==> ')
    check_menu(num_menu, lst_num)
    if num_menu == 9:
        print("Работа справочника завершена")  # почему не выводит прощание?
        exit()
    elif num_menu == 1:
        view_entry()
    elif num_menu == 2:
        add_entry()
    elif num_menu == 3:
        menu_export()
    elif num_menu == 4:
        menu_import()
    return


def menu_export():
    """
    Тут необходимо меню выбора формата експорта.
    """
    return


def menu_import():
    """
    Тут необходимо указать пользователю куда положить файл для импорта и в каких форматах.
    """
    return
