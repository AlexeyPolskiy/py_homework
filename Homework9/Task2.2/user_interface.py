from checker import check_menu, check_import
from changes_directory import *
from export_dict import *
# # from import_dict import import_directory_1, import_directory_2


def main_menu():
    create_directory()
    print("\nГлавное меню. \n"
          "1 - Действия со справочником \n"
          "2 - Экспорт справочника \n"
          "3 - Импорт справочника \n"
          "9 - Выход \n")
    num_menu = input(f"Введите номер необходимого действия ==> ")
    lst_num = ['1', '2', '3', '9']
    if check_menu(num_menu, lst_num) is True:
        if num_menu == '9':
            print('\nРабота справочника завершена')
        elif num_menu == '1':
            menu_action()
        elif num_menu == '2':
            menu_export()
        elif num_menu == '3':
            menu_import()
    else:
        print(f"\nВы ввели не корректное значение: {num_menu} \n")
        main_menu()  # тут надо подумать как вернуться в начало функции меню
    return


def menu_action():
    print("\nДействия со справочником: \n"
          "1 - Просмотр записей \n"
          "2 - Добавление записи \n"
          "3 - Поиск записи \n"
          "4 - Удаление записи \n"
          "9 - Вернуться в основное меню \n")
    lst_num = ['1', '2', '3', '4', '9']
    num_menu = input(f'Введите номер необходимого действия ==> ')
    if check_menu(num_menu, lst_num) is True:
        if num_menu == '9':
            main_menu()
        elif num_menu == '1':  # Тут просмотр справочника
            menu_view()
            menu_action()
        elif num_menu == '2':  # Тут добавление записи в справочник
            menu_add()
            menu_action()
        elif num_menu == '3':  # tyt nado poisk
            menu_search()
            menu_action()
        elif num_menu == '4':  # tut nado delete
            menu_del()
            menu_action()
    else:
        print(f" \nВы ввели не корректное значение: {num_menu}  \n")
        main_menu()
    return


def menu_view():
    print("\nТелефонный справочник:")
    print('  ', 'Имя ', 'Фамилия ', 'Номер телефона ', 'Примечание ')
    last_numb_string, lst_tel = view_entry()
    for view in lst_tel:
        print(view)
    return last_numb_string


def menu_add():
    add_str = (input(f'\nВведите имя => ') + ' ' +
               input(f'Введите фамилию => ') + ' ' +
               input(f'Введите номер => ') + ' ' +
               input(f'Введите примечание => ') + '\n')
    # print(add_str)
    add_entry(add_str)


def menu_search():
    find_str = input(f'\nВведите атрибут поиска ==> ')
    if len(find_entry(find_str)) == 0:
        print('\nРезультат поиска отрицательный!')
    else:
        for find_line in find_entry(find_str):
            print(find_line)


def menu_del():
    last_num = menu_view()
    numb_del = input("\nВведите порядковый номер контакта, который хотите удалить ==> ")
    if numb_del.isdigit() is True and int(numb_del) <= last_num:
        temp_del = input("\nВы уверены? Да/Нет: ")
        if temp_del in ['Да', 'да']:
            del_entry(int(numb_del))
        # elif temp_del in ['Нет', 'нет']:
        #     pass
    else:
        print(f"Вы ввели не корректный номер: {numb_del}")


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
    temp_imp = input("Введите ответ: ")
    if temp_imp in ['Да', 'да']:
        if check_import() is True:
            """
            if : сюда надо сделать формат txt
                import_directory_1()
            elif : сюда надо сделать формат csv
                import_directory_2()
            """
    elif temp_imp in ['Нет', 'нет']:
        main_menu()
    return
