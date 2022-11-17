

def check_menu(num, lst_):
    """
    Здесь проверяется что введены значения [1, 2, 3, 4, 9] или [1, 2] и только они
    """
    if len(num) == 1 and num.isdigit() is True and num in lst_:
        return True
    else:
        return False


def check_import():
    """
    Сюда надо проверку:
    1. Наличие файла в папке
    2. Проверка формата записи
    3. Проверка расширения файла
    """
    return