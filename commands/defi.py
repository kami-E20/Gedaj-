def register_defi(bot):
    bot.add_command('defi', lambda msg: bot.send_message(msg.chat.id, 'Commande /defi exécutée avec succès.'))
