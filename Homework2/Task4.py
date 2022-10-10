"""
Задание 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на позициях a и b.
Значения N, a и b вводит пользователь с клавиатуры.
"""
from random import randint

number_n = int(input('Задайте список из N элементов: '))
index_a = int(input('Введите позицию А => [0. N]: '))
index_b = int(input('Введите позицию В => [0. N]: '))

if index_a > number_n or index_b > number_n:
    print(f'Введите позиции А И В не более N ({number_n})')
else:
    lst_n = []
    for i in range(number_n):
        lst_n.append(randint(-number_n, number_n))
    print(lst_n)
    # print(type(lst_n))
    result_ = lst_n[index_a] * lst_n[index_b]
    print(f'Произвведение чисел с позиции А[{index_a}]= {lst_n[index_a]} и В[{index_b}]= {lst_n[index_b]} => {result_}')