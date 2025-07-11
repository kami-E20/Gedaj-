def register_forcequiz(bot):
    bot.add_command('forcequiz', lambda msg: bot.send_message(msg.chat.id, "❓ *Quiz du jour* publié immédiatement."))
