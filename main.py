import os
from telebot import TeleBot
import logging

# Debug Render : affiche le token
print(">>> BOT_TOKEN récupéré :", os.getenv("BOT_TOKEN"))

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN or ':' not in TOKEN:
    raise ValueError("Le token Telegram est invalide ou manquant. Vérifie la variable d'environnement BOT_TOKEN.")

bot = TeleBot(TOKEN)

# -------------------------
# 📦 COMMANDES UTILISATEUR
# -------------------------
from commands import (
    start, help, quiz, correction, filmdujour, suggestion, spoiler, avis, fanpass,
    classement, translate, lang, abodumois, inviter, prochainfilm, vision, defi,
    source, recompenses
)

start.register_start(bot)
help.register_help(bot)
quiz.register_quiz(bot)
correction.register_correction(bot)
filmdujour.register_filmdujour(bot)
suggestion.register_suggestion(bot)
spoiler.register_spoiler(bot)
avis.register_avis(bot)
fanpass.register_fanpass(bot)
classement.register_classement(bot)
translate.register_translate(bot)
lang.register_lang(bot)
abodumois.register_abodumois(bot)
inviter.register_inviter(bot)
prochainfilm.register_prochainfilm(bot)
vision.register_vision(bot)
defi.register_defi(bot)
source.register_source(bot)
recompenses.register_recompenses(bot)

# -------------------------
# 🛡️ COMMANDES ADMIN ONLY
# -------------------------
from commands_admin import (
    admin, adminpanel, lockdown, forcefilm, forcequiz,
    forcenews, senddebug, restorebackup, call, test
)

admin.register_admin(bot)
adminpanel.register_adminpanel(bot)
lockdown.register_lockdown(bot)
forcefilm.register_forcefilm(bot)
forcequiz.register_forcequiz(bot)
forcenews.register_forcenews(bot)
senddebug.register_senddebug(bot)
restorebackup.register_restorebackup(bot)
call.register_call(bot)
test.register_test(bot)

# -------------------------
# ▶️ LANCEMENT DU BOT
# -------------------------
if __name__ == '__main__':
    print('✅ Bot démarré avec succès...')
    bot.infinity_polling()