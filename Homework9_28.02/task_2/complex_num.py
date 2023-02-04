# import sympy


def check_complex(num: str):
    """
    z = a + bi
    """
    if '+' and 'i' in num:
        # print(num)
        return True
    else:
        # print(f"Вы ввели не корректные данные: {num}")
        return False


def view_complex(num: str):
    num = num.replace(' ', '')
    if 'i' in num:
        num = num.replace('i', 'j')
        return num
    else:
        return num


def actions_complex(num_1: str, num_2: str, action: str):
    if action == '+':
        result = complex(num_1) + complex(num_2)
        return result
    elif action == '-':
        result = complex(num_1) - complex(num_2)
        return result
    elif action == '*':
        result = complex(num_1) * complex(num_2)
        return result
    elif action == '/':
        result = complex(num_1) / complex(num_2)
        return result
    else:
        print(f"Вы ввели не корректные данные: {action}, начните сначала")
        action = input("Введите знак действия (+, -, *, /): ")
        actions_complex(num_1, num_2, action)
