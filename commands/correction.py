def register_correction(bot):
    bot.add_command('correction', lambda msg: bot.send_message(msg.chat.id, 'Commande /correction exécutée avec succès.'))
