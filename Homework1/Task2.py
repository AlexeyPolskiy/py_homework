"""
Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
"""

for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            print(f'При x = {x}, y = {y}, z = {z}')
            print(f'Вырачение {not (x or y or z) == (not x and not y and not z)};')

