import json
from datetime import datetime

ADMINS = [5618445554, 879386491]  # Liste des admins
ANNIV_FILE = "data/anniversaire.json"

def get_today_anniversaires():
    try:
        with open(ANNIV_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        return []

    today = datetime.now().strftime("%m-%d")
    return [entry for entry in data if entry["date"] == today]

def format_anniversaire_message(entry):
    return (
        f"🎉 *Anniversaire aujourd’hui !*\n"
        f"👤 *{entry['nom']}* ({entry.get('profession', 'Inconnu')})\n"
        f"🌍 {entry.get('nationalité', 'Non précisée')}\n"
        f"🎬 Connu pour : _{entry.get('connu_pour', '---')}_"
    )

def envoyer_anniversaires(bot):
    anniversaires = get_today_anniversaires()
    if not anniversaires:
        return

    for entry in anniversaires:
        msg = format_anniversaire_message(entry)
        for admin_id in ADMINS:
            bot.send_message(admin_id, msg, parse_mode="Markdown")

# Optionnel : commande manuelle
def register_anniversaire(bot):
    @bot.message_handler(commands=["anniv"])
    def cmd_anniv(message):
        if message.from_user.id in ADMINS:
            anniversaires = get_today_anniversaires()
            if not anniversaires:
                bot.reply_to(message, "Aucun anniversaire aujourd’hui.")
            else:
                for entry in anniversaires:
                    bot.send_message(message.chat.id, format_anniversaire_message(entry), parse_mode="Markdown")
