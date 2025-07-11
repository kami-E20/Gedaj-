def register_forcefilm(bot):
    bot.add_command('forcefilm', lambda msg: bot.send_message(msg.chat.id, "📽️ *Publication forcée* du film du jour déclenchée."))
