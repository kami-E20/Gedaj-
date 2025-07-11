def register_suggestion(bot):
    bot.add_command('suggestion', lambda msg: bot.send_message(msg.chat.id, 'Commande /suggestion exécutée avec succès.'))
