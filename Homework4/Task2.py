"""
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

*Пример*

- при N=236     ->        [2, 2, 59]
"""

num_ = int(input("Введите не отрицательное целое число = "))

numb_ = num_

k = 2

lst_ = []

while k <= num_:
    if num_ % k == 0:
        lst_.append(k)
        num_ = num_ // k
        k = 2
    else:
        k += 1

# print(type(num_))

print(f'При N = {numb_}   ->    {lst_}')

