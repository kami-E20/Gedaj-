def register_quiz(bot):
    @bot.message_handler(commands=['quiz'])
    def handle(message):
        bot.reply_to(message, 'Quiz du jour : Quel est le film ?')