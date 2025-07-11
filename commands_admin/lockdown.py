def register_lockdown(bot):
    bot.add_command('lockdown', lambda msg: bot.send_message(msg.chat.id, 'Commande /lockdown réservée aux admins exécutée.'))
