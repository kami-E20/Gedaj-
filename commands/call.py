def register_call(bot):
    bot.add_command('call', lambda msg: bot.send_message(msg.chat.id, 'Commande /call réservée aux admins exécutée.'))
