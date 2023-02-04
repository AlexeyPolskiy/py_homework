from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from initial_input import num_input


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    num_input()
    await update.message.reply_text(f'Какого ***???? {update.effective_user.first_name}')
