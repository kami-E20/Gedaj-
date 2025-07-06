import os
import telebot
import threading
from dotenv import load_dotenv
from web import keep_alive

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🎬 Bienvenue dans l’univers de GEDAJ 🤖\n\nIci, tu recevras chaque jour :\n— des films ou animés cultes 📺\n— des quiz cinéma pour t’amuser 🎯\n— des actus geek secrètes 🔒\n— des classements & cadeaux 🎁\n\n🤝 Tu fais maintenant partie de la communauté Geekmania.\n👉 Rejoins le canal ici : @GEEKMANIA")

@bot.message_handler(commands=['help'])
def help_cmd(message):
    bot.reply_to(message, '''📖 GUIDE D’UTILISATION – GEDAJ

Voici ce que tu peux faire avec Gedaj 🤖 :

🎬 /filmdujour – Découvre le film ou l’animation du jour
❓ /quiz – Participe au quiz ciné du jour
✅ /correction – Obtiens les réponses du dernier quiz
🎯 /defi – Relève un défi bonus pour gagner des points
🌍 /translate – Traduis un message en anglais ou français
🧠 /suggestion – Propose un film, anime ou idée à Geekmania
🎭 /spoiler – Cacher ou révéler un spoiler dans le canal
📊 /classement – Voir le top des abonnés actifs
🎁 /recompenses – Vois les cadeaux offerts aux meilleurs abonnés
👑 /abodumois – Infos sur les abonnés du mois
🧢 /fanpass – Rôles spéciaux de la communauté
💌 /inviter – Partage un lien personnalisé pour inviter tes amis
🕒 /prochainfilm – Heure de la prochaine publication
🌐 /lang – Choisir ta langue (FR / EN)
📎 /source – Voir la source du film ou actu
💬 /avis – Envoyer ton avis sur le contenu du jour
👨‍💼 /admin – Liste des admins du canal
📜 /vision – Vision et mission de Gedaj

💡 Tape simplement une commande pour l’utiliser 👇''')

if __name__ == "__main__":
    print("Gedaj v1.5 lancé avec succès !")
    threading.Thread(target=keep_alive).start()
    bot.infinity_polling()