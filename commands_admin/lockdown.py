# lockdown.py
import telebot
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

# Variable globale pour stocker l'état du confinement
is_lockdown = False

# Liste des ID administrateurs autorisés
ADMIN_IDS = [5618445554, 879386491]  # Anthony et Kâmį


@bot.message_handler(commands=["lockdown_on"])
def lockdown_on(message):
    global is_lockdown
    user_id = message.from_user.id

    if user_id in ADMIN_IDS:
        is_lockdown = True
        bot.reply_to(message, "🔒 Mode confinement activé. Le bot ne répondra qu’aux administrateurs.")
    else:
        bot.reply_to(message, "⛔ Vous n’êtes pas autorisé à activer ce mode.")


@bot.message_handler(commands=["lockdown_off"])
def lockdown_off(message):
    global is_lockdown
    user_id = message.from_user.id

    if user_id in ADMIN_IDS:
        is_lockdown = False
        bot.reply_to(message, "✅ Mode confinement désactivé. Le bot est à nouveau actif pour tous.")
    else:
        bot.reply_to(message, "⛔ Vous n’êtes pas autorisé à désactiver ce mode.")


def lockdown_check(message):
    """
    Vérifie si le mode confinement est activé et si l'utilisateur est autorisé.
    À intégrer dans les autres handlers du bot.
    """
    global is_lockdown
    user_id = message.from_user.id

    if is_lockdown and user_id not in ADMIN_IDS:
        bot.reply_to(message, "⚠️ Le bot est actuellement en mode confinement. Réessayez plus tard.")
        return False
    return True