from telegram import Update, WebAppInfo
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, ContextTypes, filters
import json
import os
from datetime import datetime

# Replace with your bot token
BOT_TOKEN = '7887486115:AAFGL50qh9I-bwABzi89UCcXiXvgsP6FGDE'

# Replace with your web app URL where you'll host the game
WEBAPP_URL = 'https://naomicodedev.github.io/Schedule/'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message with a button that opens the web app."""
    await update.message.reply_text(
        "Денис Леонтьевич",
        reply_markup={
            "inline_keyboard": [[{
                "text": "Жмите чтобы начать",
                "web_app": {"url": WEBAPP_URL}
            }]]
        }
    )

async def web_app_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle data received from the web app"""
    data = json.loads(update.effective_message.web_app_data.data)
    
    # Process the game results
    moves = data.get('moves', 0)
    pairs = data.get('pairs', 0)
    completed = data.get('completed', False)
    
    if completed:
        message = f"🎮 Игра завершена!!\n📊 Статистика:\n- Шагов: {moves}\n- Найдено пар: {pairs}"
        await update.message.reply_text(message)
    else:
        await update.message.reply_text("Прогресс игры сохранен!")

def main():
    """Start the bot."""
    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, web_app_data))

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()