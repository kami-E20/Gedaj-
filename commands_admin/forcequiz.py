from telebot import TeleBot

def register_forcequiz(bot: TeleBot, admin_ids):
    @bot.message_handler(commands=["forcequiz"])
    def handle_forcequiz(message):
        if message.from_user.id in admin_ids:
            bot.reply_to(message, "🎯 Quiz du jour publié de force !")