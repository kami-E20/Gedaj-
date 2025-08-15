# lockdown.py
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

# Variable globale pour stocker l'état du confinement
is_lockdown = False

# Liste des ID administrateurs autorisés à activer/désactiver
ADMIN_IDS = [5618445554, 879386491]  # Anthony et Kâmį

def lockdown_on(update: Update, context: CallbackContext):
    global is_lockdown
    user_id = update.effective_user.id

    if user_id in ADMIN_IDS:
        is_lockdown = True
        update.message.reply_text("🔒 Mode confinement activé. Le bot ne répondra qu’aux administrateurs.")
    else:
        update.message.reply_text("⛔ Vous n’êtes pas autorisé à activer ce mode.")

def lockdown_off(update: Update, context: CallbackContext):
    global is_lockdown
    user_id = update.effective_user.id

    if user_id in ADMIN_IDS:
        is_lockdown = False
        update.message.reply_text("✅ Mode confinement désactivé. Le bot est à nouveau actif pour tous.")
    else:
        update.message.reply_text("⛔ Vous n’êtes pas autorisé à désactiver ce mode.")

def lockdown_check(update: Update, context: CallbackContext):
    """
    Vérifie si le mode confinement est activé et si l'utilisateur est autorisé.
    À intégrer dans les autres handlers du bot.
    """
    global is_lockdown
    user_id = update.effective_user.id

    if is_lockdown and user_id not in ADMIN_IDS:
        update.message.reply_text("⚠️ Le bot est actuellement en mode confinement. Réessayez plus tard.")
        return False
    return True

# Handlers à ajouter dans le main.py
lockdown_handlers = [
    CommandHandler("lockdown_on", lockdown_on),
    CommandHandler("lockdown_off", lockdown_off)
]