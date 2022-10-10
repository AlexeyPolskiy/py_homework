"""
Задание 5 Реализуйте алгоритм перемешивания списка.
"""
from random import randint


def mix_list(list_original):
    lst_ = list_original[:]
    lst_length = len(lst_)
    for n in range(lst_length):
        index_rand = randint(0, lst_length - 1)
        temp = lst_[n]
        lst_[n] = lst_[index_rand]
        lst_[index_rand] = temp
    return lst_


number_n = int(input('Задайте список из N элементов: '))

lst_n = []
for i in range(number_n):
    lst_n.append(randint(-number_n, number_n))
print(lst_n)

# mix_list(lst_n)
print(mix_list(lst_n))
