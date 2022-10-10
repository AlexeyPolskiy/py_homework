"""
Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""

from random import randint

numb_n = int(input(f'Введите количество элементов N: '))
lst_ = []
lst_sort = []
sum = 0

for i in range(numb_n):
    rand_n = randint(0, 9)
    lst_.append(rand_n)
    if i % 2 == 0:
        sum += rand_n
        lst_sort.append(rand_n)

print(f'- {lst_} -> на нечётных позициях элементы {lst_sort}, ответ: {sum}')
