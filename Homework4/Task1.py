"""
Вычислить число π c заданной точностью d

*Пример:*

- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
"""

accu_ = int(input("Введите количество знаков после запятой (не более 14): "))
k = 2
n = 0
count_ = 0
const_ = 0

while n < 10000:
    temp_1 = 4 / (k * (k + 1) * (k + 2)) - 4 / ((k + 2) * (k + 3) * (k + 4))  # метод Нилаката
    const_ += temp_1
    count_ += 1
    k += 4
    n += 1
pi_float = const_ + 3

# pi_str = str(pi_float)

# print(len(pi_str))

print(str(pi_float)[:(2 + accu_)])