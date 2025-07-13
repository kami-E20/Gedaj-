import os
from telebot import TeleBot
import logging

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN or ':' not in TOKEN:
    raise ValueError("Le token Telegram est invalide ou manquant. Vérifie la variable d'environnement BOT_TOKEN.")

bot = TeleBot(TOKEN)

# Importation des handlers enrichis
from start import start
from help import help
from quiz import quiz
from correction import correction
from filmdujour import filmdujour
from suggestion import suggestion
from spoiler import spoiler
from avis import avis
from fanpass import fanpass
from classement import classement
from admin import admin
from translate import translate
from lang import lang
from abodumois import abodumois
from inviter import inviter
from prochainfilm import prochainfilm
from vision import vision
from defi import defi
from source import source
from recompenses import recompenses
from call import call
from test import test
from forcefilm import forcefilm
from forcequiz import forcequiz
from forcenews import forcenews
from restorebackup import restorebackup
from senddebug import senddebug
from adminpanel import adminpanel
from lockdown import lockdown


if __name__ == '__main__':
    print('✅ Bot démarré avec succès...')
    bot.infinity_polling()
