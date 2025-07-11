def register_forcequiz(bot):
    bot.add_command('forcequiz', lambda msg: bot.send_message(msg.chat.id, 'Commande /forcequiz réservée aux admins exécutée.'))
