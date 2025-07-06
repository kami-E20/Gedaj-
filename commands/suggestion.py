def register_suggestion(bot):
    @bot.message_handler(commands=['suggestion'])
    def handle(message):
        bot.reply_to(message, 'Merci pour ta suggestion !')