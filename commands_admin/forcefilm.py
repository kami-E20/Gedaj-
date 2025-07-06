from telebot import TeleBot

def register_forcefilm(bot: TeleBot, admin_ids):
    @bot.message_handler(commands=["forcefilm"])
    def handle_forcefilm(message):
        if message.from_user.id in admin_ids:
            bot.reply_to(message, "🎬 Film du jour publié de force !")