"""
Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""

# lst_float = [1.1, 1.2, 3.1, 5, 10.01]
#
# lst_result = []
#
# if i % 1 != 0:
#     for i in lst_float:
#         lst_result.append(round(i % 1, 2))

# print(round(lst_float[2] % 1, 2))
#
# a = 0
#
# float_max = 0
#
# float_min = 10
#
# for i in range(len(lst_float)):
#     # print(i)
#     if float_max < round(lst_float[i] - int(lst_float[i]), 2):
#         float_max = round(lst_float[i] - int(lst_float[i]), 2)
#     if float_min > round(lst_float[i] - int(lst_float[i]), 2):
#         float_min = round(lst_float[i] - int(lst_float[i]), 2)
#
# print(float_max)
# print(float_min)

# lst = list(map(float, input("Введите числа через пробел:\n").split()))

lst_float = [1.1, 1.2, 3.1, 5, 10.01]
new_lst = [round(i % 1, 2) for i in lst_float if i % 1 != 0]
print(lst_float)
print(new_lst)
print(max(new_lst) - min(new_lst))