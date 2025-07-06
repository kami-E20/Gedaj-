from telebot import TeleBot
from datetime import date, timedelta

def register_correction(bot: TeleBot):
    @bot.message_handler(commands=["correction"])
    def handle_correction(message):
        yesterday = (date.today() - timedelta(days=1)).strftime("%d/%m/%Y")
        bot.reply_to(message, f"✅ Réponse du quiz du {yesterday} : *A. Nolan*", parse_mode="Markdown")