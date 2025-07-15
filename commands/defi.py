import json
import os
from datetime import datetime

def get_current_week_number():
    """Retourne la semaine du mois (1 à 4)"""
    today = datetime.today()
    day = today.day
    return min(((day - 1) // 7) + 1, 4)

def get_defi_du_moment():
    semaine = get_current_week_number()
    path = f"data/defis/semaine{semaine}.json"

    if not os.path.exists(path):
        return None, None, None

    with open(path, "r", encoding="utf-8") as f:
        defi = json.load(f)

    return defi.get("titre"), defi.get("contenu"), defi.get("type")

def register_defi(bot):
    @bot.message_handler(commands=['defi'])
    def handle_defi(message):
        titre, contenu, type_defi = get_defi_du_moment()

        if not titre:
            bot.send_message(message.chat.id, "⚠️ Aucun défi n'est disponible cette semaine.")
            return

        intro = f"🎯 *{titre}* — *Semaine {get_current_week_number()}*\n\n"

        if type_defi == "texte":
            bot.send_message(message.chat.id, intro + contenu, parse_mode="Markdown")
        elif type_defi == "image":
            bot.send_photo(message.chat.id, contenu, caption=intro, parse_mode="Markdown")
        elif type_defi == "audio":
            bot.send_audio(message.chat.id, contenu, caption=intro, parse_mode="Markdown")
        else:
            bot.send_message(message.chat.id, intro + contenu, parse_mode="Markdown")