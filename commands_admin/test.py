from telebot import TeleBot

def register_test(bot: TeleBot, admin_ids):
    @bot.message_handler(commands=["test"])
    def handle_test(message):
        if message.from_user.id in admin_ids:
            bot.reply_to(message, "✅ Test de Gedaj réussi. Le bot est fonctionnel.")