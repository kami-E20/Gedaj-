from telebot import TeleBot

def register_filmdujour(bot: TeleBot):
    @bot.message_handler(commands=["filmdujour"])
    def handle_film(message):
        bot.reply_to(message, "🎬 *Film du jour :*\nInception (2010)\nUn rêve dans un rêve... avec DiCaprio et la réalisation de Christopher Nolan.", parse_mode="Markdown")