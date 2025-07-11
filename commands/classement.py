def register_classement(bot):
    bot.add_command('classement', lambda msg: bot.send_message(msg.chat.id, 'Commande /classement exécutée avec succès.'))
