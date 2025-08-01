from telebot import TeleBot

AUTHORIZED_ADMINS = [5618445554, 879386491]

def register_admin(bot: TeleBot):
    @bot.message_handler(commands=['admin'])
    def handle_admin(message):
        if message.from_user.id not in AUTHORIZED_ADMINS:
            bot.reply_to(message, "⛔ Cette commande est réservée aux administrateurs.")
            return

        bot.send_message(message.chat.id, "✅ Tu es bien authentifié comme administrateur Geekmania.")