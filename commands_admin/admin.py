from telebot import types
from loader import bot, ADMINS
from scheduler import lancer_taches_scheduled
from scripts.backup import backup_donnees
from scripts.restore import restore_backup
from lockdown import lockdown_mode, unlock_mode
from filmdujour import publier_film_force
from scripts.publish import run_all

# ✅ Vérifie si l'utilisateur est admin
def is_admin(user_id):
    return str(user_id) in ADMINS


# 🔒 Mettre le bot en mode confinement
@bot.message_handler(commands=["lockdown"])
def cmd_lockdown(message):
    if not is_admin(message.from_user.id):
        return bot.reply_to(message, "⛔ Cette commande est réservée aux administrateurs.")
    lockdown_mode()
    bot.reply_to(message, "🚨 Le bot est maintenant en mode confinement.")


# 🔓 Désactiver le mode confinement
@bot.message_handler(commands=["unlock"])
def cmd_unlock(message):
    if not is_admin(message.from_user.id):
        return bot.reply_to(message, "⛔ Cette commande est réservée aux administrateurs.")
    unlock_mode()
    bot.reply_to(message, "✅ Le bot est sorti du mode confinement.")


# 🔄 Lancer toutes les tâches manuellement
@bot.message_handler(commands=["run_all"])
def cmd_run_all(message):
    if not is_admin(message.from_user.id):
        return bot.reply_to(message, "⛔ Cette commande est réservée aux administrateurs.")
    run_all(bot)
    bot.reply_to(message, "🚀 Toutes les tâches programmées ont été exécutées manuellement.")


# 💾 Sauvegarde manuelle
@bot.message_handler(commands=["backup"])
def cmd_backup(message):
    if not is_admin(message.from_user.id):
        return bot.reply_to(message, "⛔ Cette commande est réservée aux administrateurs.")
    backup_donnees(bot)
    bot.reply_to(message, "💾 Sauvegarde des données effectuée avec succès.")


# 📂 Restauration depuis backup
@bot.message_handler(commands=["restore"])
def cmd_restore(message):
    if not is_admin(message.from_user.id):
        return bot.reply_to(message, "⛔ Cette commande est réservée aux administrateurs.")
    restore_backup(bot)
    bot.reply_to(message, "📂 Les données ont été restaurées depuis le backup.")


# 🎬 Forcer la publication d’un film du jour
@bot.message_handler(commands=["forcefilm"])
def cmd_force_film(message):
    if not is_admin(message.from_user.id):
        return bot.reply_to(message, "⛔ Cette commande est réservée aux administrateurs.")
    publier_film_force(bot)
    bot.reply_to(message, "🎬 Film du jour publié de force.")


# 🧪 Test des notifications admin
@bot.message_handler(commands=["test"])
def cmd_test(message):
    if not is_admin(message.from_user.id):
        return bot.reply_to(message, "⛔ Cette commande est réservée aux administrateurs.")

    for admin_id in ADMINS:
        try:
            bot.send_message(admin_id, "🧪 Test réussi : le bot peut vous envoyer des notifications privées.")
        except Exception as e:
            print(f"❌ Erreur en envoyant au compte admin {admin_id} :", e)

    bot.reply_to(message, "✅ Test des notifications administrateurs terminé.")