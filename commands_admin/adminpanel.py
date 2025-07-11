def register_adminpanel(bot):
    bot.add_command('adminpanel', lambda msg: bot.send_message(msg.chat.id, 'Commande /adminpanel réservée aux admins exécutée.'))
