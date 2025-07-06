def register_lang(bot):
    @bot.message_handler(commands=['lang'])
    def handle(message):
        bot.reply_to(message, 'Langue définie sur Français 🇫🇷')