# import random
#
#
# degree = int(input('Введите максимальную степень: '))
# equation = {}
# for i in range(degree, -1, -1):
#     equation[i] = random.randint(-10, 10)
# print(equation)
#
def decode(equation: dict):
    new_equation = []
    for key, value in equation.items():
        if value != 0:
            new_equation.append(f'{value}*x**{key}')
    new_equation = ' ' + ' + '.join(new_equation) + ' = 0'
    new_equation = new_equation.replace('+ -', '- ')\
        .replace('*x**0', '') \
        .replace(' 1*x', ' x') \
        .replace('-1*x', '-x') \
        .replace('x**1 ', 'x ')
    # print(type(new_equation))
    return new_equation
#
#
# def create_file(equation: str, file_name: str):
#     with open(f'{file_name}.txt', 'w', encoding="utf-8") as file:
#         file.write(equation)
#
#
# def read_file(file_name: str):
#     with open(f'{file_name}.txt', 'r', encoding="utf-8") as file:
#         temp_equation = file.read()
#     return temp_equation
#
#
# equation_lst = {10: -1, 9: -3, 8: -1, 7: -4, 6: 10, 5: 2, 4: 6, 3: 6, 2: -10, 1: -1, 0: 9}
# equation_str = '-x**10 - 3*x**9 - x**8 - 4*x**7 + 10*x**6 + 2*x**5 + 6*x**4 + 6*x**3 - 10*x**2 - x + 9 = 0'
#
# # create_file(equation_str, 'file_2')
# print(read_file('file_1'))
#
#
# def encode(equation: str):
#     print(equation)
#     equation = (' ' + equation).replace(' + ', ' ')
#     print(f'1. {equation}')
#     equation = equation.replace(' - ', ' -')
#     print(f'2. {equation}')
#     equation = equation.replace(' -x', ' -1*x')
#     print(f'3. {equation}')
#     equation = equation.replace(' x', ' 1*x')
#     print(f'4. {equation}')
#     equation = equation.replace('*x ', '*x**1 ').split()[:-2]
#     print(f'5. {equation}')
#     dict_equation = {}
#     for item in equation:
#         print(item)
#         i = item.split('*x**')
#         print(i)
#         if len(i) > 1:
#             dict_equation[int(i[1])] = int(i[0])
#         elif len(i) == 1 and i[0] != '':
#             dict_equation[0] = int(i[0])
#         print(dict_equation)
#     return dict_equation

# equation_str = '-x**10 - 3*x**9 - x**8 - 4*x**7 + 10*x**6 + 2*x**5 + 6*x**4 + 6*x**3 - 10*x**2 - x + 9 = 0'
# print(encode(equation_str))


def addition(eq_first: dict, eq_second: dict):
    eq_result = {}
    eq_result.update(eq_first)
    eq_result.update(eq_second)
    for key in eq_result:
        eq_result[key] = eq_first.get(key, 0) + eq_second.get(key, 0)
    return eq_result


eq_first = {10: -1, 9: -3, 8: -1, 7: -4, 6: 10, 5: 2, 4: 6, 3: 6, 2: -10, 1: -1, 0: 9}
eq_second = {10: 5, 9: -1, 8: 1, 7: 0, 6: -4, 5: 12, 4: 4, 3: 0, 2: -10, 1: -12, 0: 12}

result = addition(eq_first, eq_second)
print(decode(eq_first))
print(decode(eq_second))
print(result)
print(decode(result))

