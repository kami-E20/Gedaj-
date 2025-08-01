import os
from telebot import TeleBot

# 🔐 Lecture du token depuis les variables d’environnement
BOT_TOKEN = os.getenv("BOT_TOKEN")

# ⚠️ En cas d’oubli de configuration
if not BOT_TOKEN:
    raise ValueError("❌ Le token du bot n’a pas été défini. Vérifie la variable d’environnement BOT_TOKEN.")

# 🤖 Initialisation du bot
bot = TeleBot(BOT_TOKEN)