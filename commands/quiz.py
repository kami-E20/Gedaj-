def register_quiz(bot):
    bot.add_command('quiz', lambda msg: bot.send_message(msg.chat.id, 'Commande /quiz exécutée avec succès.'))
