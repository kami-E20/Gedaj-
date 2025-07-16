# scripts/notify_anniversaires.py

import os
from telebot import TeleBot
from anniversary import format_anniversaire_message

def notify_admins_anniversaires():
    # Récupération des IDs admin depuis variable d’environnement ou valeur par défaut
    admin_ids = os.getenv("ADMINS", "879386491,5618445554")
    admin_ids = [int(uid.strip()) for uid in admin_ids.split(",")]

    # Initialisation du bot
    TOKEN = os.getenv("BOT_TOKEN")
    if not TOKEN or ":" not in TOKEN:
        print("❌ Erreur : token Telegram invalide.")
        return

    bot = TeleBot(TOKEN)

    # Création du message
    message = format_anniversaire_message()

    # Envoi à chaque admin
    for admin_id in admin_ids:
        try:
            bot.send_message(admin_id, message, parse_mode="Markdown")
            print(f"✅ Message anniversaire envoyé à l’admin {admin_id}")
        except Exception as e:
            print(f"❌ Échec d’envoi à {admin_id} :", e)

# Lancement direct si exécuté manuellement
if __name__ == "__main__":
    notify_admins_anniversaires()