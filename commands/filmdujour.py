def register_filmdujour(bot):
    bot.add_command('filmdujour', lambda msg: bot.send_message(msg.chat.id, 'Commande /filmdujour exécutée avec succès.'))
