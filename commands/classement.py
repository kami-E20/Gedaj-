def register_classement(bot):
    bot.add_command('classement', lambda msg: bot.send_message(msg.chat.id, "📊 Voici le *top 10 des abonnés les plus actifs* cette semaine !"))
