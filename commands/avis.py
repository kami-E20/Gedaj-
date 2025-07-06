def register_avis(bot):
    @bot.message_handler(commands=['avis'])
    def handle(message):
        bot.reply_to(message, 'Ton avis a été transmis aux admins 💬')