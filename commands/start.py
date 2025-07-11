def register_start(bot):
    bot.add_command('start', lambda msg: bot.send_message(msg.chat.id, 'Commande /start exécutée avec succès.'))
