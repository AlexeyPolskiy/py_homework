import random


def create_equation(degree: int):
    equation = {}
    for i in range(degree, -1, -1):
        equation[i] = random.randint(-10, 10)
    # print(equation)
    return equation
