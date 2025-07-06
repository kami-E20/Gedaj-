def register_inviter(bot):
    @bot.message_handler(commands=['inviter'])
    def handle_inviter(message):
        user_id = message.from_user.id
        invite_link = f"https://t.me/GEEKMANIA?start={user_id}"
        msg = (
            "📨 Invite tes amis à rejoindre Geekmania !

"
            f"🔗 Ton lien personnel : {invite_link}

"
            "🎁 Des récompenses sont prévues pour les meilleurs parrains !"
        )
        bot.reply_to(message, msg)