from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from complex_num import *
from real_num import *
from log import log_temp

temp = ''


async def num_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    temp = ''
    num_1 = input("Введите первое число: ")
    action = input("Введите знак действия (+, -, *, /): ")
    num_2 = input("Введите второе число: ")
    if check_complex(num_1) is True and check_complex(num_2) is True:
        num_1 = view_complex(num_1)
        num_2 = view_complex(num_2)
        result = actions_complex(num_1, num_2, action)
        result = str(result)[1:-1]
        log_temp(num_1, action, num_2, result)
        # print(str(result)[1:-1])
        return result
    else:
        num_1 = view_real(num_1)
        num_2 = view_real(num_2)
        result = actions_real(num_1, num_2, action)
        log_temp(num_1, action, num_2, result)
        return result
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


# def num_input():
#     num_1 = input("Введите первое число: ")
#     action = input("Введите знак действия (+, -, *, /): ")
#     num_2 = input("Введите второе число: ")
#     if check_complex(num_1) is True and check_complex(num_2) is True:
#         num_1 = view_complex(num_1)
#         num_2 = view_complex(num_2)
#         result = actions_complex(num_1, num_2, action)
#         result = str(result)[1:-1]
#         log_temp(num_1, action, num_2, result)
#         # print(str(result)[1:-1])
#         return result
#     else:
#         num_1 = view_real(num_1)
#         num_2 = view_real(num_2)
#         result = actions_real(num_1, num_2, action)
#         log_temp(num_1, action, num_2, result)
#         return result


