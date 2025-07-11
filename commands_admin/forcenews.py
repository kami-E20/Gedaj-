def register_forcenews(bot):
    bot.add_command('forcenews', lambda msg: bot.send_message(msg.chat.id, "📰 *Actu Geekmania* du jour envoyée en privé aux admins."))
