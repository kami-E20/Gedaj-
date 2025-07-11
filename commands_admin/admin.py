def register_admin(bot):
    bot.add_command('admin', lambda msg: bot.send_message(msg.chat.id, 'Commande /admin exécutée avec succès.'))
