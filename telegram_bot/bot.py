import os
import sys
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dh_generator import generate_dh_parameters

load_dotenv()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        'Hello. Use /generate [KEY] command to generate parameters.'
    )


async def generate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        key = context.args[0]
        if key == os.getenv('KEY'):
            parameters = generate_dh_parameters()
            await update.message.reply_text(parameters)
        else:
            await update.message.reply_text('Incorrect key')
    except IndexError:
        await update.message.reply_text('Key not found')


app = ApplicationBuilder().token(os.getenv('TOKEN')).build()
app.add_handler(CommandHandler('start', start))
app.add_handler(CommandHandler('generate', generate))
app.run_polling()
