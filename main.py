import os
import telebot
from web import keep_alive

# Import commandes utilisateurs
from commands.quiz import register_quiz
from commands.correction import register_correction
from commands.filmdujour import register_filmdujour
from commands.suggestion import register_suggestion
from commands.defi import register_defi
from commands.translate import register_translate
from commands.spoiler import register_spoiler
from commands.classement import register_classement
from commands.recompenses import register_recompenses
from commands.abodumois import register_abodumois
from commands.fanpass import register_fanpass
from commands.inviter import register_inviter
from commands.prochainfilm import register_prochainfilm
from commands.lang import register_lang
from commands.source import register_source
from commands.avis import register_avis
from commands.start import register_start
from commands.help import register_help
from commands.vision import register_vision
from commands.textlistener import register_gedaj_listener

# Import commandes admin
from commands_admin.test import register_test
from commands_admin.forcefilm import register_forcefilm
from commands_admin.forcequiz import register_forcequiz
from commands_admin.forcenews import register_forcenews
from commands_admin.restorebackup import register_restorebackup
from commands_admin.senddebug import register_senddebug
from commands_admin.sorties import register_sorties
from commands_admin.anniversaire import register_anniversaire
from commands_admin.admin import register_admin

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

# Enregistrer les commandes utilisateurs
register_start(bot)
register_help(bot)
register_vision(bot)
register_quiz(bot)
register_correction(bot)
register_filmdujour(bot)
register_suggestion(bot)
register_defi(bot)
register_translate(bot)
register_spoiler(bot)
register_classement(bot)
register_recompenses(bot)
register_abodumois(bot)
register_fanpass(bot)
register_inviter(bot)
register_prochainfilm(bot)
register_lang(bot)
register_source(bot)
register_avis(bot)
register_gedaj_listener(bot)

# Enregistrer les commandes admin
admin_ids = [879386491, 5618445554]
register_test(bot, admin_ids)
register_forcefilm(bot, admin_ids)
register_forcequiz(bot, admin_ids)
register_forcenews(bot, admin_ids)
register_restorebackup(bot, admin_ids)
register_senddebug(bot, admin_ids)
register_sorties(bot, admin_ids)
register_anniversaire(bot, admin_ids)
register_admin(bot, admin_ids)

# Lancer serveur web
keep_alive()

# Démarrage du bot
print("Gedaj lancé avec succès !")
bot.infinity_polling()