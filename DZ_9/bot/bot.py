from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *
app = ApplicationBuilder().token(
    "5517358212:AAGRIw8sK7NrrrHp_sjhtDUVfzLVkpnrYzk").build()

app.add_handler(CommandHandler("hello", hello_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("calc", calc_command))
print('Start bot')
app.run_polling()
