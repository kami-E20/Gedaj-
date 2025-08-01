import os
from telebot import TeleBot
from scripts.publish import publier_film

AUTHORIZED_ADMINS = [5618445554, 879386491]  # Anthony & Kâmį

def register_forcefilm(bot: TeleBot):
    @bot.message_handler(commands=['forcefilm'])
    def handle_force_film(message):
        if message.from_user.id not in AUTHORIZED_ADMINS:
            bot.reply_to(message, "⛔ Cette commande est réservée aux administrateurs.\nUtilise /call ou /suggestion pour contacter l’équipe.")
            return

        publier_film(bot)
        bot.send_message(message.chat.id, "🎬 Film du jour publié manuellement.")