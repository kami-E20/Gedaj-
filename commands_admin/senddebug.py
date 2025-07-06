from telebot import TeleBot

def register_senddebug(bot: TeleBot, admin_ids):
    @bot.message_handler(commands=["senddebug"])
    def handle_senddebug(message):
        if message.from_user.id in admin_ids:
            bot.reply_to(message, "📤 Logs envoyés aux administrateurs.")