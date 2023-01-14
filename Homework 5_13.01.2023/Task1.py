# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


first_str = 'Изучение полиномиАБВльных урАБВвнений и их решений долгое время составляло едва ли не \
глАБВвный объект классической АБВлгебры. '

except_ = "АБВ"

result_lst = list(filter(lambda x: except_ not in x, first_str.split(" ")))
# print(result_lst)
result_ = " ".join(result_lst)

print(f" {first_str} \n {result_}")
