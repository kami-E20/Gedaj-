def register_defi(bot):
    bot.add_command('defi', lambda msg: bot.send_message(msg.chat.id, "🎯 Défi bonus du jour : réponds correctement et gagne +10 points !"))
