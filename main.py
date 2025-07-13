import os
from telebot import TeleBot
import logging

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN or ':' not in TOKEN:
    raise ValueError("Le token Telegram est invalide ou manquant. Vérifie la variable d'environnement BOT_TOKEN.")

bot = TeleBot(TOKEN)

# Importation des fichiers de commandes
import start
import help
import quiz
import correction
import filmdujour
import suggestion
import spoiler
import avis
import fanpass
import classement
import admin
import translate
import lang
import abodumois
import inviter
import prochainfilm
import vision
import defi
import source
import recompenses
import call
import test
import forcefilm
import forcequiz
import forcenews
import restorebackup
import senddebug
import adminpanel
import lockdown


if __name__ == '__main__':
    print('✅ Bot démarré avec succès...')
    bot.infinity_polling()
