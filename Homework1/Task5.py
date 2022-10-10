"""
Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

Пример:

- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
"""

from math import *


def distance(x1, y1, x2, y2):
    c = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return c


x1 = float(input('введите координату х точки А = '))
y1 = float(input('введите координату y точки А = '))
x2 = float(input('введите координату х точки B = '))
y2 = float(input('введите координату y точки B = '))

print(f'A ({x1},{y1}); B ({x2},{y2}) -> {round(float(distance(x1, y1, x2, y2)), 2)}')
