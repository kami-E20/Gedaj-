import os
from telebot import TeleBot
from scripts.publish import publier_quiz

AUTHORIZED_ADMINS = [5618445554, 879386491]  # Anthony & Kâmį

def register_forcequiz(bot: TeleBot):
    @bot.message_handler(commands=['forcequiz'])
    def handle_force_quiz(message):
        if message.from_user.id not in AUTHORIZED_ADMINS:
            bot.reply_to(message, "⛔ Cette commande est réservée aux administrateurs.\nUtilise /call ou /suggestion pour contacter l’équipe.")
            return

        publier_quiz(bot)
        bot.send_message(message.chat.id, "✅ Quiz du jour publié manuellement.")