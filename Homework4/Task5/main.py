from create_equation import create_equation
from decoding import decode
from encoding import encode
from addition import addition
from actions_files import create_file, read_file


if __name__ == '__main__':
    degree_1 = int(input('Введите максимальную степень для первого уравнения ==> '))
    equation_1 = create_equation(degree_1)
    print(f"Первое уравнение: \n{decode(equation_1)}\n")
    create_file(decode(equation_1), 'file_1')
    degree_2 = int(input('Введите максимальную степень для второго уравнения ==> '))
    equation_2 = create_equation(degree_2)
    print(f"Второе уравнение: \n{decode(equation_2)}\n")
    create_file(decode(equation_2), 'file_2')
    equation_1 = read_file('file_1')
    equation_2 = read_file('file_2')
    result_equation = addition(encode(equation_1), encode(equation_2))
    print(f"Результат сложения двух уравнений: \n{decode(result_equation)}")
    create_file(decode(result_equation), 'result')
