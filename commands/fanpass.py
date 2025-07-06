def register_fanpass(bot):
    @bot.message_handler(commands=['fanpass'])
    def handle(message):
        bot.reply_to(message, 'Fan Pass activé 🎫')