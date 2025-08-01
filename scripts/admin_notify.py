import os
from telebot import TeleBot
from datetime import datetime

def send_admin_news(bot: TeleBot, news: dict, categorie="Actu"):
    admin_ids = [int(uid.strip()) for uid in os.getenv("ADMINS", "879386491,5618445554").split(",")]
    date_str = datetime.now().strftime("%d/%m/%Y")

    msg = (
        f"🎬 [ACTU GEEKMANIA DU JOUR] – {date_str}\n\n"
        f"🧩 Catégorie : {categorie}\n"
        f"🗞️ Titre : {news.get('titre', 'Sans titre')}\n"
        f"📌 Résumé : {news.get('description', '')[:250]}...\n"
        f"🔗 Source : {news.get('lien', 'Aucune')}"
    )

    for admin_id in admin_ids:
        if 'image' in news:
            bot.send_photo(admin_id, news['image'], caption=msg)
        else:
            bot.send_message(admin_id, msg)