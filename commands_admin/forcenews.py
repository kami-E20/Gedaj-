from telebot import TeleBot
from scripts.publish import publier_actu_privee

AUTHORIZED_ADMINS = [5618445554, 879386491]

def register_forcenews(bot: TeleBot):
    @bot.message_handler(commands=['forcenews'])
    def handle_forcenews(message):
        if message.from_user.id not in AUTHORIZED_ADMINS:
            bot.reply_to(message, "⛔ Réservé aux admins. Utilise /call pour contacter l’équipe.")
            return

        publier_actu_privee(bot)
        bot.send_message(message.chat.id, "🗞️ Actualité privée envoyée aux administrateurs.")