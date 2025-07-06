def register_start(bot):
    @bot.message_handler(commands=['start'])
    def handle(message):
        bot.reply_to(message, 'Bienvenue dans GEDAJ 🎬')