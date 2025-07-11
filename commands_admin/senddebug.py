def register_senddebug(bot):
    bot.add_command('senddebug', lambda msg: bot.send_message(msg.chat.id, "📤 Logs et status du bot envoyés à l’admin principal."))
