from telebot import TeleBot

def register_sorties(bot: TeleBot, admin_ids):
    @bot.message_handler(commands=["sorties"])
    def handle_sorties(message):
        if message.from_user.id in admin_ids:
            bot.reply_to(message, "🎬 Prochaines sorties envoyées.")