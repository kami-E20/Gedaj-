import json
import os
from datetime import datetime

DEFI_FILE = "data/defis.json"

def get_current_context():
    """Retourne année, mois texte (ex: juillet), et semaine"""
    now = datetime.now()
    year = str(now.year)
    mois = now.strftime("%B").lower()  # ex: 'juillet'
    semaine = f"semaine_{min(((now.day - 1) // 7) + 1, 4)}"
    return year, mois, semaine

def get_defi_du_moment():
    if not os.path.exists(DEFI_FILE):
        return None, None, None

    try:
        with open(DEFI_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        year, mois, semaine = get_current_context()
        defi = data.get(year, {}).get(mois, {}).get(semaine, {})

        return defi.get("titre"), defi.get("description"), defi.get("type")
    except Exception as e:
        print("❌ Erreur lecture défi :", e)
        return None, None, None

def register_defi(bot):
    @bot.message_handler(commands=['defi'])
    def handle_defi(message):
        titre, contenu, type_defi = get_defi_du_moment()

        if not titre:
            bot.send_message(message.chat.id, "⚠️ Aucun défi n'est disponible cette semaine.")
            return

        semaine = get_current_context()[2][-1]  # Récupère le numéro (ex: '4' depuis 'semaine_4')
        intro = f"🎯 *{titre}* — *Semaine {semaine}*\n\n"

        if type_defi == "texte":
            bot.send_message(message.chat.id, intro + contenu, parse_mode="Markdown")
        elif type_defi == "image":
            bot.send_photo(message.chat.id, contenu, caption=intro, parse_mode="Markdown")
        elif type_defi == "audio":
            bot.send_audio(message.chat.id, contenu, caption=intro, parse_mode="Markdown")
        else:
            bot.send_message(message.chat.id, intro + contenu, parse_mode="Markdown")