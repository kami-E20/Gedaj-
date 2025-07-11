def register_inviter(bot):
    bot.add_command('inviter', lambda msg: bot.send_message(msg.chat.id, "💌 Invite tes amis et gagne des points !\nVoici ton lien personnalisé : https://t.me/GEEKMANIA?start=tonpseudo"))
