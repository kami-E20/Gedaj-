import os
from telebot import TeleBot, types

TOKEN = os.getenv("BOT_TOKEN")
bot = TeleBot(TOKEN)