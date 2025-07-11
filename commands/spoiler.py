def register_spoiler(bot):
    bot.add_command('spoiler', lambda msg: bot.send_message(msg.chat.id, "⚠️ Le message suivant est un *spoiler*.\nClique sur « Afficher » pour le voir."))
