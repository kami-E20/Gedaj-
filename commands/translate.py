def register_translate(bot):
    @bot.message_handler(commands=['translate'])
    def handle(message):
        bot.reply_to(message, 'Traduction activée 🌐')