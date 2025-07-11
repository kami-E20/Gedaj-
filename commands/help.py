def register_help(bot):
    bot.add_command('help', lambda msg: bot.send_message(msg.chat.id, 'Commande /help exécutée avec succès.'))
