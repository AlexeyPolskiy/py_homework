"""
Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной
последовательности.

*Пример*

- при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]

lst_ = [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]
result_ = []
for i in lst_:
    if lst_.count(i) == 1:
        result_.append(i)
print(f'- при {lst_}     ->        {result_}')
"""

lst_ = [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]
result_ = [i for i in lst_ if lst_.count(i) == 1]
print(f'- при {lst_}     ->        {result_}')
