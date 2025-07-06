import telebot
import os
from web import keep_alive

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Bienvenue sur Gedaj 🤖 ! Utilise /help pour voir ce que je peux faire.")

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "🤖 *Commandes disponibles :*

"
        "/start - Message d’accueil chaleureux
"
        "/help - Affiche ce message d’aide
"
        "Répond aussi au mot 'gedaj' automatiquement selon l’utilisateur.

"
        "Et bien plus à venir sur Geekmania 🎬 !"
    )
    bot.send_message(message.chat.id, help_text, parse_mode="Markdown")

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