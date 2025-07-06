def register_correction(bot):
    @bot.message_handler(commands=['correction'])
    def handle(message):
        bot.reply_to(message, 'La réponse du quiz précédent était : A')