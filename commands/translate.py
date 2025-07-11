def register_translate(bot):
    bot.add_command('translate', lambda msg: bot.send_message(msg.chat.id, 'Commande /translate exécutée avec succès.'))
