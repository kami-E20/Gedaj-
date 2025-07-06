def register_filmdujour(bot):
    @bot.message_handler(commands=['filmdujour'])
    def handle(message):
        bot.reply_to(message, 'Film du jour : Inception')