def register_senddebug(bot):
    bot.add_command('senddebug', lambda msg: bot.send_message(msg.chat.id, 'Commande /senddebug réservée aux admins exécutée.'))
