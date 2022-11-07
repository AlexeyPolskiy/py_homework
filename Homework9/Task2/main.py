import telebot.types
from telebot import TeleBot


bot = TeleBot('5650069881:AAEbr6jqcGhfTREkbECV-mbhrXTbe6MdsnI')


@bot.message_handler()
def echo(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=f'Вы прислали: {msg.text}')


bot.polling()