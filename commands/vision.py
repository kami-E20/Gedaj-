def register_vision(bot):
    bot.add_command('vision', lambda msg: bot.send_message(msg.chat.id, 'Commande /vision exécutée avec succès.'))
