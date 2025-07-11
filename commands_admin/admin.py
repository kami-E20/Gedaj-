def register_admin(bot):
    bot.add_command('admin', lambda msg: bot.send_message(msg.chat.id, "👨‍💼 Admins officiels de @GEEKMANIA :\n• Kâmį\n• Anthony\nPour contacter l’équipe, utilise /suggestion."))
