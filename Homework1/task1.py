"""
Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

Пример:

- 6 -> да
- 7 -> да
- 1 -> нет
"""


number_of_days = int(input('Введите номер дня недели: \n'))

if 1 <= number_of_days <= 5:
    print('Это рабочий день недели')
    
elif 6 <= number_of_days <= 7:
    print('Это выходной')
    
else:
    print(f'Нет такого номера дня недели ({number_of_days})')