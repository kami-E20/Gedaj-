import os
from telebot import TeleBot
from datetime import datetime

def send_admin_news(bot: TeleBot, news, categorie="Actu"):
    from_env = os.getenv("ADMINS", "879386491,5618445554")
    admin_ids = [int(uid.strip()) for uid in from_env.split(",")]

    date_str = datetime.now().strftime("%d/%m/%Y")
    msg = (
        f"🎬 [ACTU GEEKMANIA DU JOUR] – {date_str}\n\n"
        f"🧩 Catégorie : {categorie}\n"
        f"🗞️ Titre : {news['titre']}\n"
        f"📌 Résumé : {news['description'][:250]}...\n"
        f"🔗 Source : {news.get('lien', 'Aucune')}"
    )
    for admin_id in admin_ids:
        bot.send_message(admin_id, msg)
        if 'image' in news:
            bot.send_photo(admin_id, news['image'])