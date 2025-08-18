# loader.py
import os
from telebot import TeleBot

# 🔐 Lecture du token depuis les variables d’environnement
BOT_TOKEN = os.getenv("BOT_TOKEN")

# ⚠️ Vérification stricte
if not BOT_TOKEN:
    raise ValueError("❌ Le token du bot n’a pas été défini. Vérifie la variable d’environnement BOT_TOKEN.")

# 🤖 Initialisation du bot
bot = TeleBot(BOT_TOKEN)

# 👑 IDs des administrateurs (Anthony & Kâmį)
ADMINS = [5618445554, 879386491]

# 📂 Chemins utiles
DATA_DIR = "data"
BACKUP_DIR = "backup"

# 📌 Fonction utilitaire : vérifier si un user est admin
def is_admin(user_id: int) -> bool:
    return user_id in ADMINS

# ➕ Commande utilitaire : afficher son ID
@bot.message_handler(commands=["id"])
def send_user_id(message):
    bot.reply_to(message, f"👤 Ton ID est : `{message.from_user.id}`", parse_mode="Markdown")