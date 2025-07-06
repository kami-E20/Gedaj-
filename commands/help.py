def register_help(bot):
    @bot.message_handler(commands=['help'])
    def handle(message):
        bot.reply_to(message, 'Voici les commandes disponibles...')