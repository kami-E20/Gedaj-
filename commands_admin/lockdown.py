import os
import telebot

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

# Variable globale pour le mode confinement
is_lockdown = False

# Liste des admins
ADMIN_IDS = [5618445554, 879386491]

@bot.message_handler(commands=["lockdown_on"])
def lockdown_mode(message):
    global is_lockdown
    if message.from_user.id in ADMIN_IDS:
        is_lockdown = True
        bot.reply_to(message, "🔒 Mode confinement activé. Le bot ne répondra qu’aux administrateurs.")
    else:
        bot.reply_to(message, "⛔ Vous n’êtes pas autorisé à activer ce mode.")

@bot.message_handler(commands=["lockdown_off"])
def unlock_mode(message):
    global is_lockdown
    if message.from_user.id in ADMIN_IDS:
        is_lockdown = False
        bot.reply_to(message, "✅ Mode confinement désactivé. Le bot est à nouveau actif pour tous.")
    else:
        bot.reply_to(message, "⛔ Vous n’êtes pas autorisé à désactiver ce mode.")

def lockdown_check(message):
    """
    Vérifie si le mode confinement est activé et si l'utilisateur est autorisé.
    À appeler dans les autres handlers.
    """
    global is_lockdown
    if is_lockdown and message.from_user.id not in ADMIN_IDS:
        bot.reply_to(message, "⚠️ Le bot est actuellement en mode confinement. Réessayez plus tard.")
        return False
    return True