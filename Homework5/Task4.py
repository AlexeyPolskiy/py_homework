"""
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
"""


def compress(txt):
    count = 1
    result_txt = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            result_txt = result_txt + str(count) + txt[i] + ' '
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        result_txt = result_txt + str(count) + txt[-1]
    return result_txt


def decompress(txt):
    number = ''
    result_txt = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            result_txt = result_txt + txt[i] * int(number)
            number = ''
    return result_txt


str_ = "WWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWqWWWWWWWWWWW"
print(compress(str_))
print(decompress(compress(str_)))
