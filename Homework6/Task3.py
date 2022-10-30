"""
Задание 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Пример:

6782 -> 23
0,56 -> 11


number_ = str(input('Введите вещественное число: '))
sum_ = 0
for i in number_:
    if i != '.':
        sum_ = sum_ + int(i)
print(sum_)
"""

number_ = input('Введите вещественное число: ')
# result = [char for char in number_]
lst_sort = list(map(int, filter(lambda x: x != '.', [number_[i] for i in range(len(number_))])))
# print(lst_sort)
# print(result)
print(sum(lst_sort, 0))
