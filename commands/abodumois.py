import json
import os
from datetime import datetime

ABO_FILE = "data/abonne_du_mois.json"

def get_abonne_du_mois():
    if not os.path.exists(ABO_FILE):
        return None

    with open(ABO_FILE, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return None

    nom = data.get("nom", "—")
    description = data.get("description", "—")
    photo_url = data.get("photo_url", None)

    if not nom or not description:
        return None

    return nom, description, photo_url

def register_abodumois(bot):
    @bot.message_handler(commands=['abodumois'])
    def handle_abodumois(message):
        result = get_abonne_du_mois()
        if not result:
            bot.send_message(message.chat.id, "⚠️ Aucun abonné du mois n’a encore été désigné.")
            return

        nom, description, photo_url = result
        mois = datetime.now().strftime("%B %Y")

        texte = (
            f"🏅 *Abonné du mois – {mois}*\n\n"
            f"👏 Félicitations à *{nom}* !\n\n"
            f"{description}\n\n"
            "_Merci pour ta fidélité et ta participation active sur Geekmania !_"
        )

        if photo_url:
            bot.send_photo(message.chat.id, photo_url, caption=texte, parse_mode="Markdown")
        else:
            bot.send_message(message.chat.id, texte, parse_mode="Markdown")