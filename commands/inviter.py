def register_inviter(bot):
    @bot.message_handler(commands=['inviter'])
    def handle_inviter(message):
        bot.send_message(
            message.chat.id,
            "📩 Invite tes amis à rejoindre Geekmania !\n"
            "Utilise ce lien pour partager : https://t.me/GedajBot?start=invite"
        )