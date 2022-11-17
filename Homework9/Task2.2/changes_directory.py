import os


def create_directory():
    first_line = ['Ключ ', 'Имя ', 'Фамилия ', 'Номер телефона ', 'Примечание ']
    if os.path.exists('tel_directory.txt') is not True:
        temp = open('tel_directory.txt', "w")
        temp.writelines(first_line)
        temp.close()


def view_entry():
    """
    Просмотр записей справочника
    """
    return


def add_entry():
    """
    Добавление записи справочника
    """
    return


def del_entry():
    """
    Удаление записи справочника
    """
    return


def find_entry():
    """
    Поиск по фамилии, номеру телефона записи
    """
    return
