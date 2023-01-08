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
    # print(new_equation)
    return new_equation[1:]
