import os
import telebot
from web import keep_alive

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🎬 Bienvenue dans l’univers de GEDAJ 🤖\n\nIci, tu recevras chaque jour :\n— des films ou animés cultes 📺\n— des quiz cinéma pour t’amuser 🎯\n— des actus geek secrètes 🔒\n— des classements & cadeaux 🎁\n\n🤝 Tu fais maintenant partie de la communauté Geekmania.\n👉 Rejoins le canal ici : @GEEKMANIA")

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "📖 *COMMANDES DISPONIBLES*\n\n"
        "/start - Message d’accueil\n"
        "/help - Affiche ce guide\n"
        "/vision - Découvre la mission de Gedaj\n"
        "Écris simplement 'gedaj' et je te réponds selon qui tu es 😉"
    )
    bot.send_message(message.chat.id, help_text, parse_mode="Markdown")

@bot.message_handler(commands=['vision'])
def handle_vision(message):
    bot.reply_to(message, "👁️ Ma vision est de rendre le cinéma et l’animation accessibles, fun et communautaires, tous les jours avec Geekmania !")

@bot.message_handler(func=lambda message: 'gedaj' in message.text.lower())
def detect_gedaj(message):
    user_id = message.from_user.id
    if user_id == 879386491:  # Kami
        bot.reply_to(message, "Oui papa 😎")
    elif user_id == 5618445554:  # Anthony
        bot.reply_to(message, "Oui tonton 😄")
    else:
        bot.reply_to(message, "Présent chef ✋")

keep_alive()
print("Gedaj lancé avec succès !")
bot.infinity_polling()
