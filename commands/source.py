def register_source(bot):
    bot.add_command('source', lambda msg: bot.send_message(msg.chat.id, 'Commande /source exécutée avec succès.'))
