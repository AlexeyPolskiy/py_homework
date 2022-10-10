"""
Задание 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
округлённую до трёх знаков после точки.

Пример:

Для n = 6 -> 14.072
"""

number_ = int(input('Введите число N: '))
# print(type(number_))
sum_lst = 0
for i in range(1, number_ + 1):
    sum_lst += (1 + 1/i) ** i
    # print(round(sum_lst, 3))
print(f'Для n = {number_} -> {round(sum_lst, 3)}')