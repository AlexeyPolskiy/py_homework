def check_real(num: str):
    return


def view_real(num: str):
    num = num.replace(',', '.')
    return num


def actions_real(num_1: str, num_2: str, action: str):
    if action == '+':
        result = float(num_1) + float(num_2)
        return result
    elif action == '-':
        result = float(num_1) - float(num_2)
        return result
    elif action == '*':
        result = float(num_1) * float(num_2)
        return result
    elif action == '/':
        result = float(num_1) / float(num_2)
        return result
    else:
        print(f"Вы ввели не корректные данные: {action}, начните сначала")
        action = input("Введите знак действия (+, -, *, /): ")
        actions_real(num_1, num_2, action)
