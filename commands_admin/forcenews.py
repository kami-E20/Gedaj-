def register_forcenews(bot):
    bot.add_command('forcenews', lambda msg: bot.send_message(msg.chat.id, 'Commande /forcenews réservée aux admins exécutée.'))
