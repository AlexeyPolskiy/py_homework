"""
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""


def feb(k):
    feb_lst = [1, 0, 1]
    f_1 = 0
    f_2 = 1
    for i in range(2, k + 1):
        feb_pos = f_1 + f_2
        f_1, f_2 = f_2, feb_pos
        feb_lst.append(feb_pos)
    feb_neg_lst = []
    f_1 = 0
    f_2 = 1
    for i in range(2, k + 1):
        feb_neg = f_1 - f_2
        f_1, f_2 = f_2, feb_neg
        feb_neg_lst.append(feb_neg)
    feb_neg_lst.reverse()
    feb_neg_lst.extend(feb_lst)
    return feb_neg_lst


int_k = int(input("Задайте число = "))
print(feb(int_k))
