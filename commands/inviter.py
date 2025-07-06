def register_inviter(bot):
    @bot.message_handler(commands=['inviter'])
    def handle(message):
        bot.reply_to(message, 'Voici ton lien d’invitation : https://t.me/GEEKMANIA')