def register_recompenses(bot):
    bot.add_command('recompenses', lambda msg: bot.send_message(msg.chat.id, 'Commande /recompenses exécutée avec succès.'))
