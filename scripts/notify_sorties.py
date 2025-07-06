import os
from telebot import TeleBot

def notify_sorties(bot: TeleBot, sorties, categorie="Sortie"):
    if not sorties:
        return
    admin_ids = [int(x) for x in os.getenv("ADMINS", "879386491,5618445554").split(",")]
    for s in sorties:
        texte = (
            f"🔮 [SORTIE À VENIR] – {s['date']}\n\n"
            f"🎬 {s['titre']}\n"
            f"🧠 {s['description'][:250]}...\n"
            f"🔗 {s['lien']}"
        )
        for admin in admin_ids:
            bot.send_message(admin, texte)
            if s.get("image"):
                bot.send_photo(admin, s["image"])