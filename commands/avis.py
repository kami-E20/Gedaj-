def register_avis(bot):
    bot.add_command('avis', lambda msg: bot.send_message(msg.chat.id, "💬 Tu peux maintenant donner ton *avis* sur le film ou le quiz du jour.\nMerci de ton retour !"))
