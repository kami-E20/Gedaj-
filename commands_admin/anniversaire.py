from telebot import TeleBot

def register_anniversaire(bot: TeleBot, admin_ids):
    @bot.message_handler(commands=["anniversaire"])
    def handle_anniversaire(message):
        if message.from_user.id in admin_ids:
            bot.reply_to(message, "🎉 Liste des anniversaires envoyée.")