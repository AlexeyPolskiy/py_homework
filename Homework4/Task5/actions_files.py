def create_file(equation: str, file_name: str):
    with open(f'{file_name}.txt', 'w', encoding="utf-8") as file:
        file.write(equation)


def read_file(file_name: str):
    with open(f'{file_name}.txt', 'r', encoding="utf-8") as file:
        temp_equation = file.read()
    return temp_equation
