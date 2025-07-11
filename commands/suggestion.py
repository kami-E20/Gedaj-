def register_suggestion(bot):
    bot.add_command('suggestion', lambda msg: bot.send_message(msg.chat.id, "🧠 Tu as un film ou anime à recommander ?\nEnvoie ton idée ici, elle sera transmise aux admins."))
