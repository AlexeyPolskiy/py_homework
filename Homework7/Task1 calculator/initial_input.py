from complex_num import *
from  real_num import *


def num_input():
    num_1 = input("Введите первое число: ")
    action = input("Введите знак действия (+, -, *, /): ")
    num_2 = input("Введите второе число: ")
    if check_complex(num_1) is True and check_complex(num_2) is True:
        num_1 = view_complex(num_1)
        num_2 = view_complex(num_2)
        result = actions_complex(num_1, num_2, action)
        print(type(result))
        print(result)
    else:
        result = actions_real(num_1, num_2, action)
        print(result)
