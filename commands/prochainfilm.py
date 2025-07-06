def register_prochainfilm(bot):
    @bot.message_handler(commands=['prochainfilm'])
    def handle(message):
        bot.reply_to(message, 'Prochaine diffusion à 15h 📅')