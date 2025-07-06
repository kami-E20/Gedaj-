def register_vision(bot):
    @bot.message_handler(commands=['vision'])
    def handle(message):
        bot.reply_to(message, 'Ma vision est de rendre le cinéma accessible à tous.')