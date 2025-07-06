def register_classement(bot):
    @bot.message_handler(commands=['classement'])
    def handle(message):
        bot.reply_to(message, 'Top 5 des abonnés 🎖️')