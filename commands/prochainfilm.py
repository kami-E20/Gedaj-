def register_prochainfilm(bot):
    bot.add_command('prochainfilm', lambda msg: bot.send_message(msg.chat.id, 'Commande /prochainfilm exécutée avec succès.'))
