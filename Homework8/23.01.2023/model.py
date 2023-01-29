import view

# employees
{1: {'ФИО': 'Иван Иванов', 'Должность': 'должность'}, }

# task
{1: {'Рабочее задание': 'рабочее задание', 'Бригадир': 'id_employees', 'Рабочий': 'id_employees',
     'Статус': 'в работе'}, }

"""
# purpose
{1: {'Цель': 'Постановка цели', 'Статус': 'не выполнено'}, }
"""

# id_count_employees = 0
# id_count_task = 0
#
# employees = {}
# task = {}

"""
id_count_purpose = 0
"""


#
# def add_new_employees():
#     new_employee = dict()
#     new_employee['Id'] = get_new_id()
#     new_employee["ФИО"] = view.view_func("ФИО")
#     new_employee["Должность"] = view.view_func("должность")

def add_new_employees():
    """Тут наполняем базу сотрудников"""
    pass


def save_new_employees():
    """тут сохраняем словарь сотрудников в файл employees.csv"""
    pass


def add_new_tasks():
    """тут наполняем базу """
    pass
