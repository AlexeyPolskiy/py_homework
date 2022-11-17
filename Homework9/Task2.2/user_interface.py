from checker import check_menu, check_import
from changes_directory import *
# from export_dict import export_directory_1, export_directory_2
# # from import_dict import import_directory_1, import_directory_2


def main_menu():
    create_directory()
    print("Главное меню. \n"
          "1 - Просмотр записей справочника \n"
          "2 - Добавление записи в справочник \n"
          "3 - Экспорт справочника \n"
          "4 - Импорт справочника \n"
          "9 - Выход \n")
    num_menu = input(f"Введите номер необходимого действия ==> ")
    lst_num = ['1', '2', '3', '4', '9']
    if check_menu(num_menu, lst_num) is True:
        if num_menu == '9':
            print('\nРабота справочника завершена')
        elif num_menu == '1':
            view_entry()
        elif num_menu == '2':
            add_entry()
        elif num_menu == '3':
            menu_export()
        elif num_menu == '4':
            menu_import()
    else:
        print(f"\nВы ввели не корректное значение: {num_menu} \n")
        main_menu()  # тут надо подумать как вернуться в начало функции меню
    return


def menu_export():
    """
    Тут необходимо меню выбора формата экспорта.
    """
    print("Меню экспорта: \n"
          "1 - Экспортировать в формате csv \n"
          "2 - Экспортировать в формате txt \n"
          "9 - Вернуться в основное меню \n")
    lst_num = ['1', '2', '9']
    num_menu = input(f'Введите номер необходимого действия ==> ')
    if check_menu(num_menu, lst_num) is True:
        if num_menu == 9:
            main_menu()
        elif num_menu == 1:
            export_directory_1()
        elif num_menu == 2:
            export_directory_2()
    else:
        print(f" \nВы ввели не корректное значение: {num_menu}  \n")
        main_menu()
    return


def menu_import():
    """
    Тут необходимо указать пользователю куда положить файл для импорта и в каких форматах.
    """
    print("Импортируемый файл должны быть: \n"
          "1. размещен в папке /Homework9/Task2.2/import \n"
          "2. иметь следующий формат записи [ , Имя, Фамилия, номер телефона, комментарий] \n"
          "3. иметь имя файла import_directory \n"
          "4. иметь расширение .csv или .txt \n"
          "Запустить импорт? (Да/Нет) \n")
    temp = input("Введите ответ: ")
    if temp in ['Да', 'да']:
        if check_import() is True:
            """
            if : сюда надо сделать формат txt
                import_directory_1()
            elif : сюда надо сделать формат csv
                import_directory_2()
            """
    elif temp in ['Нет', 'нет']:
        main_menu()
    return
