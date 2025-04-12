from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, MessageHandler, filters, CommandHandler, ContextTypes
import logging
import platform
import asyncio
import requests
from dotenv import load_dotenv
import os

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
API_URL = 'http://127.0.0.1:8000/api/currencies/'

# Buttons
keyboard = [
    [KeyboardButton("All Banks")],
    [KeyboardButton("Amonatbonk"), KeyboardButton("Eskhata")],
    [KeyboardButton("Arvand"), KeyboardButton("Imon")],
    [KeyboardButton("Oriyonbonk")]
]
reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Select a bank to receive exchange rates:", reply_markup=reply_markup)

# Message processing
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text.strip().lower()

    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            data = response.json()
            message = ""

            if text == "all banks":
                message = "Exchange rates of all banks:\n\n"
                for currency, info in data.items():
                    message += f"{currency}:\n"
                    for key, value in info['data'].items():
                        message += f"{key}: {value}\n"
                    message += f"Source: {info['source']}\n\n"
            else:
                message = f"Exchange rates — {text.title()}:\n\n"
                found = False
                for currency, info in data.items():
                    if info['source'].lower() == text:
                        found = True
                        message += f"{currency}:\n"
                        for key, value in info['data'].items():
                            message += f"{key}: {value}\n"
                        message += "\n"
                if not found:
                    message += "No data available for this bank."

            await update.message.reply_text(message)
        else:
            await update.message.reply_text("Failed to get data from API.")
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {e}")

# Launch
async def main():
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    await application.initialize()
    await application.start()
    await application.updater.start_polling()
    logger.info("Bot launched")
    await asyncio.Event().wait()

# Launch
if __name__ == '__main__':
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())