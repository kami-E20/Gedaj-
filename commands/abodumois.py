import json
import os

ABO_FILE = "data/abonne_du_mois.json"

def get_abonne_du_mois():
    if not os.path.exists(ABO_FILE):
        return None
    with open(ABO_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("nom"), data.get("description"), data.get("photo_url")

def register_abodumois(bot):
    @bot.message_handler(commands=['abodumois'])
    def handle_abodumois(message):
        nom, description, photo_url = get_abonne_du_mois()
        if nom:
            texte = (
                f"🏅 *Abonné du mois*\n\n"
                f"Félicitations à *{nom}* ! 🎉\n\n"
                f"{description}\n\n"
                "Merci pour ta fidélité et ta participation active sur Geekmania !"
            )
            if photo_url:
                bot.send_photo(message.chat.id, photo_url, caption=texte, parse_mode="Markdown")
            else:
                bot.send_message(message.chat.id, texte, parse_mode="Markdown")
        else:
            bot.send_message(message.chat.id, "Aucun abonné du mois n’a encore été désigné.")