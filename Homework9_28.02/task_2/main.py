from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

TOKEN_API = "5650069881:AAEbr6jqcGhfTREkbECV-mbhrXTbe6MdsnI"


app = ApplicationBuilder().token(TOKEN_API).build()

print("fuck bot")

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("start", start))

app.run_polling()
