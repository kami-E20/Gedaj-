from telebot import TeleBot

def register_suggestion(bot: TeleBot):
    @bot.message_handler(commands=["suggestion"])
    def handle_suggestion(message):
        bot.reply_to(message, "💡 Merci pour ta suggestion ! Elle a bien été transmise aux admins.")