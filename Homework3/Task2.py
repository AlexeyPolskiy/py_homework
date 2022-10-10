"""
Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
"""

lst_ = [2, 3, 4, 5, 62, 3, 4, 5, 62, 3, 4, 5, 6]

lst_result = []

result_ = 1

a = 0

# print(len(lst_))
# print(int(round((len(lst_) / 2) + 0.25)))

for i in range(int(round((len(lst_) / 2) + 0.25))):
    result_ = lst_[a] * lst_[len(lst_) - 1 - a]
    a += 1
    lst_result.append(result_)

print(f'- {lst_} => {lst_result}')