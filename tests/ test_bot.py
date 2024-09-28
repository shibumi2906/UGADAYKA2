from telegram_bot.handlers.start_handler import start
from telegram import Update, Bot

def test_start_handler():
    update = Update(update_id=123, message="start")
    bot = Bot(token="TOKEN")
    result = start(update, bot)
    assert result == "Welcome to the bot!"
