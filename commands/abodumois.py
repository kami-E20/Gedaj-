def register_abodumois(bot):
    @bot.message_handler(commands=['abodumois'])
    def handle(message):
        bot.reply_to(message, 'Abonné du mois : 👑')