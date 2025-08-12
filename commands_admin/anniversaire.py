import json
from datetime import datetime
from telebot import TeleBot

# Liste des administrateurs
ADMINS = [5618445554, 879386491]

# Fichier JSON contenant tous les anniversaires
ANNIV_FILE = "data/anniversaire.json"

def get_today_anniversaires():
    """Retourne la liste des anniversaires correspondant à la date du jour."""
    try:
        with open(ANNIV_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

    today = datetime.now().strftime("%m-%d")
    return [entry for entry in data if entry.get("date") == today]

def format_anniversaire_message(entry):
    """Formate le message d'anniversaire."""
    return (
        f"🎉 *Anniversaire aujourd’hui !*\n"
        f"👤 *{entry.get('nom', 'Inconnu')}* ({entry.get('profession', 'Non précisée')})\n"
        f"🌍 {entry.get('nationalité', 'Non précisée')}\n"
        f"🎬 Connu pour : _{entry.get('connu_pour', '---')}_"
    )

def envoyer_anniversaires(bot: TeleBot):
    """Envoie les anniversaires du jour aux administrateurs uniquement."""
    anniversaires = get_today_anniversaires()
    if not anniversaires:
        return

    for entry in anniversaires:
        msg = format_anniversaire_message(entry)
        for admin_id in ADMINS:
            try:
                bot.send_message(admin_id, msg, parse_mode="Markdown")
            except Exception as e:
                print(f"Erreur lors de l'envoi à {admin_id}: {e}")

def register_anniversaire(bot: TeleBot):
    """Commande manuelle /anniv réservée aux admins."""
    @bot.message_handler(commands=["anniv"])
    def cmd_anniv(message):
        if message.from_user.id not in ADMINS:
            bot.reply_to(message, "🚫 Cette commande est réservée aux administrateurs.")
            return

        anniversaires = get_today_anniversaires()
        if not anniversaires:
            bot.reply_to(message, "Aucun anniversaire aujourd’hui.")
            return

        for entry in anniversaires:
            bot.send_message(message.chat.id, format_anniversaire_message(entry), parse_mode="Markdown")