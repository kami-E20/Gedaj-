def register_lang(bot):
    bot.add_command('lang', lambda msg: bot.send_message(msg.chat.id, 'Commande /lang exécutée avec succès.'))
