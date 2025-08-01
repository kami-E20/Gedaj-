from telebot import TeleBot

AUTHORIZED_ADMINS = [5618445554, 879386491]

def register_adminpanel(bot: TeleBot):
    @bot.message_handler(commands=['adminpanel'])
    def handle_adminpanel(message):
        if message.from_user.id not in AUTHORIZED_ADMINS:
            bot.reply_to(message, "⛔ Cette commande est réservée aux administrateurs.")
            return

        bot.send_message(message.chat.id, "📊 Accès au panneau admin confirmé.")