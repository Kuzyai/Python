from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime as dt
from spy import *
from operator import mul, truediv, sub, add
import re


async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await logger(update, context)
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await logger(update, context)
    await update.message.reply_text(f'/hello - Приветствие\n/help - Справка\n/time - Текущее время\n/calc - Калькулятор')


async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await logger(update, context)
    await update.message.reply_text(f'{dt.now().time().strftime("%H:%M:%S")}')


async def calc_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await logger(update, context)
    try:
        s = ''.join(update.message.text.split()[1:])
        result = list(filter(lambda x: x != '', re.split(
            r'(\d+|[()])', re.sub(r'\s', '', s))))

        def parentheses(s):
            list_index_start = [i for i in range(len(s)) if s[i] == '(']
            for i in list_index_start[::-1]:
                for j in range(i+1, len(s)):
                    if s[j] == ')':
                        return i+1, j

        def calculation(s, i=0, j=len(result)):
            def replacement(f):
                nonlocal i, j
                n = str(f(float(s[i - 1]), float(s[i + 1])))
                del s[i - 1:i + 2]
                s.insert(i - 1, n)
                i -= 1
                j -= 2
            while '(' in s[i:j]:
                ret = parentheses(s)
                calculation(s, ret[0], ret[1])
                del s[ret[0] + 1]
                del s[ret[0] - 1]
                j = len(s)
            while j - i > 1:
                temp = i
                while i < j:
                    if s[i] == '*':
                        replacement(mul)
                    elif s[i] == '/':
                        replacement(truediv)
                    i += 1
                    if len(s) == 1:
                        return s
                i = temp
                while i < j:
                    if s[i] == '+':
                        replacement(add)
                    elif s[i] == '-':
                        replacement(sub)
                    i += 1
                    if len(s) == 1:
                        return s
            return s
        calc = str(round(float(''.join(calculation(result))), 2))
        await update.message.reply_text(f'{calc}')
    except ValueError:
        await update.message.reply_text(
            f'Введенные значения не являются цифрами, введите выражение в формате /calc <выражение>')
