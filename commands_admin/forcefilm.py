def register_forcefilm(bot):
    bot.add_command('forcefilm', lambda msg: bot.send_message(msg.chat.id, 'Commande /forcefilm réservée aux admins exécutée.'))
