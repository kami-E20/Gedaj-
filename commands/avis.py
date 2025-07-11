def register_avis(bot):
    bot.add_command('avis', lambda msg: bot.send_message(msg.chat.id, 'Commande /avis exécutée avec succès.'))
