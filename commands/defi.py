def register_defi(bot):
    @bot.message_handler(commands=['defi'])
    def handle(message):
        bot.reply_to(message, 'Voici ton défi du jour 💥')