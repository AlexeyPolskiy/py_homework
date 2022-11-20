# find_str = input(f'\nВведите атрибут поиска ==> ')
# result_find = []
# with open(r"tel_directory.txt", 'r', encoding="utf-8") as file:
#     for line_numb, line in enumerate(file, start=1):
#         if find_str in line:
#             result_find.append(str(line_numb) + '. ' + line[:(-1)])
# print(result_find)
#
# print(len(result_find))
#
# for find_line in result_find:
#     print(find_line)

# del_line = 1
# with open(r"temp.txt", "r", encoding="utf-8") as file:
#     lines = file.readlines()
#     print(lines)
# del lines[del_line - 1]
# with open(r"temp.txt", "w", encoding="utf-8") as file:
#     print(lines)
#     file.writelines(lines)


temp_lst = []
with open('temp.txt', 'r', encoding="utf-8") as file:
    for line_numb, line in enumerate(file, start=1):
        temp_lst.append(str(line_numb) + '. ' + line[:(-1)])
print((temp_lst, line_numb))
lst_, last_number = (temp_lst, line_numb)
print(lst_)
print(last_number)
print(type(last_number))
