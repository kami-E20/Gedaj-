def register_test(bot):
    bot.add_command('test', lambda msg: bot.send_message(msg.chat.id, 'Commande /test réservée aux admins exécutée.'))
