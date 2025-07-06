import telebot
import os
from telebot import types
from scheduler import run_scheduler
import threading
from commands.start import register_start
from commands.help import register_help
from commands.quiz import register_quiz
from commands.listener import register_listener
from commands.classement import register_classement
from commands.recompenses import register_recompenses
from commands.abodumois import register_abodumois

# Charger le token depuis les variables d'environnement
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

# Enregistrer les commandes utilisateur
register_start(bot)
register_help(bot)
register_quiz(bot)
register_listener(bot)
register_classement(bot)
register_recompenses(bot)
register_abodumois(bot)

# Démarrer la planification dans un thread parallèle
threading.Thread(target=run_scheduler, daemon=True).start()

# Lancer le bot
bot.infinity_polling()