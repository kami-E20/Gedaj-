def register_recompenses(bot):
    @bot.message_handler(commands=['recompenses'])
    def handle(message):
        bot.reply_to(message, 'Récompenses mensuelles : 🎁')