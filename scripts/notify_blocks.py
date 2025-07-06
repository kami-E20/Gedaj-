import os
from telebot import TeleBot
from datetime import datetime

def send_admin_anniv(bot: TeleBot, liste):
    from_env = os.getenv("ADMINS", "879386491,5618445554")
    admin_ids = [int(uid.strip()) for uid in from_env.split(",")]
    date_str = datetime.now().strftime("%d/%m/%Y")

    if not liste:
        return

    message = f"🎂 [ANNIVERSAIRES DU JOUR] – {date_str}\n\n"
    for perso in liste:
        message += f"👤 {perso['nom']} (né en {perso['annee']})\n🎬 Reco : {perso.get('film', '–')}\n🧠 {perso.get('note', '')}\n\n"

    for admin_id in admin_ids:
        bot.send_message(admin_id, message)

def send_admin_sorties(bot: TeleBot, liste):
    from_env = os.getenv("ADMINS", "879386491,5618445554")
    admin_ids = [int(uid.strip()) for uid in from_env.split(",")]
    if not liste:
        return
    for media in liste:
        texte = (
            f"🔮 [SORTIE À VENIR] – {media['date']}\n\n"
            f"🎬 {media['titre']}\n"
            f"🧠 {media['description'][:250]}...\n"
            f"🔗 {media['lien']}"
        )
        for admin_id in admin_ids:
            bot.send_message(admin_id, texte)
            bot.send_photo(admin_id, media["image"])