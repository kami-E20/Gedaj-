def register_inviter(bot):
    bot.add_command('inviter', lambda msg: bot.send_message(msg.chat.id, 'Commande /inviter exécutée avec succès.'))
