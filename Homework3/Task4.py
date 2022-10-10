"""
Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10

переделай на список!!!
"""

numb_ = int(input('Введите число N = '))

lst_bin = []
str_bin = ''
n = numb_

while numb_ > 0:
    lst_bin.append(str(numb_ % 2))
    numb_ = numb_ // 2

str_bin = ''.join(lst_bin)
print(f'- {n} -> {str_bin}')