from telebot import TeleBot

def register_forcenews(bot: TeleBot, admin_ids):
    @bot.message_handler(commands=["forcenews"])
    def handle_forcenews(message):
        if message.from_user.id in admin_ids:
            bot.reply_to(message, "🗞️ Actu du jour publiée de force !")