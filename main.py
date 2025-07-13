import os
from telebot import TeleBot
import logging

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN or ':' not in TOKEN:
    raise ValueError("Le token Telegram est invalide ou manquant. Vérifie la variable d'environnement BOT_TOKEN.")

bot = TeleBot(TOKEN)

# Import des commandes utilisateur
from commands import start
from commands import help
from commands import quiz
from commands import correction
from commands import filmdujour
from commands import suggestion
from commands import spoiler
from commands import avis
from commands import fanpass
from commands import classement
from commands import translate
from commands import lang
from commands import abodumois
from commands import inviter
from commands import prochainfilm
from commands import vision
from commands import defi
from commands import source
from commands import recompenses
from commands import call
from commands import test
from commands import forcefilm
from commands import forcequiz
from commands import forcenews
from commands import restorebackup
from commands import senddebug

# Import des commandes admin
from commands_admin import admin
from commands_admin import adminpanel
from commands_admin import lockdown


if __name__ == '__main__':
    print('✅ Bot démarré avec succès...')
    bot.infinity_polling()
