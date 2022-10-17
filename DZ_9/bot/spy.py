from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime as dt


async def logger(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    path = 'C:\\Users\\ognev\\Desktop\\Python_2\\DZ_9\\bot\\bd.csv'
    with open(path, 'a', encoding='utf-8') as file:
        file.write(
            f'{dt.now().strftime(r"%d.%m.%Y-%H:%M")};{update.effective_user.first_name};{update.effective_user.id};{update.message.text}\n')
