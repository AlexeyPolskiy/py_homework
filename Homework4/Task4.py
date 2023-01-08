"""
Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
и записать в файл многочлен степени k.

*Пример:*

- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
"""

import random

k = int(input("Введите коэффициент k: "))

array_ = []

for i in range(k + 1):
    numb_rand = int(random.randint(0, 100))
    if numb_rand == 0:
        continue
    elif numb_rand > 0:
        if len(array_) > 0:
            array_.append(" + ")
    if k - i > 1:
        array_.append((str(f'{abs(numb_rand)}x^{k - i}')))
    elif k - i == 1:
        array_.append((str(f'{abs(numb_rand)}x')))
    else:
        array_.append((str(abs(numb_rand))))

array_.append(" = 0")

with open('Task4.txt', 'a') as file:
    file.write("".join(array_) + "\n")
