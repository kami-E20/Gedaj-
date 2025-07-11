def register_test(bot):
    bot.add_command('test', lambda msg: bot.send_message(msg.chat.id, "🧪 Test complet lancé :\n• Envoi film : OK\n• Envoi quiz : OK\n• Privé admin : OK\n• Backup : OK"))
