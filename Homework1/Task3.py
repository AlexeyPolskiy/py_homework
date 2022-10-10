"""
    Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

    Пример:

    - x=34; y=-30 -> 4
    - x=2; y=4-> 1
    - x=-34; y=-30 -> 3
"""

coordinate_x = int(input("Введите координату точки Х: \n"))
coordinate_y = int(input("Введите координату точки Y: \n"))

if coordinate_x == 0 and coordinate_y != 0:
    print('Точка на оси Х')
    exit(0)
elif coordinate_x != 0 and coordinate_y == 0:
    print('Точка на оси Y')
    exit(0)
if coordinate_x == 0 and coordinate_y == 0:
    print('Точка в центе, введите другие координаты')
    exit(0)
if coordinate_x > 0 and coordinate_y > 0:
    quarters = 1
elif coordinate_x < 0 and coordinate_y > 0:
    quarters = 2
elif coordinate_x < 0 and coordinate_y < 0:
    quarters = 3
elif coordinate_x > 0 and coordinate_y < 0:
    quarters = 4
    print(f'Точка с координатами x = {coordinate_x}; y = {coordinate_y} находится в {quarters} четверти')
