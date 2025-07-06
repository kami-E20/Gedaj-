def register_spoiler(bot):
    @bot.message_handler(commands=['spoiler'])
    def handle(message):
        bot.reply_to(message, '⚠️ Spoiler masqué')