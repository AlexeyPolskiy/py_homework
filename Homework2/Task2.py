"""
Задание 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

Пример:

пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
"""

number_ = int(input('Введите число N: '))
result_ = 1
num_lst = []
for i in range(1, number_+1):
    result_ *= i
    num_lst.append(result_)
print(f'пусть N = {number_}, тогда {num_lst}')