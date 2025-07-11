def register_fanpass(bot):
    bot.add_command('fanpass', lambda msg: bot.send_message(msg.chat.id, 'Commande /fanpass exécutée avec succès.'))
