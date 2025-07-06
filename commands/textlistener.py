def register_gedaj_listener(bot):
    @bot.message_handler(func=lambda msg: 'gedaj' in msg.text.lower())
    def handle(message):
        user_id = message.from_user.id
        if user_id == 879386491:
            bot.reply_to(message, 'Oui papa 😎')
        elif user_id == 5618445554:
            bot.reply_to(message, 'Oui tonton 😄')
        else:
            bot.reply_to(message, 'Présent chef ✋')