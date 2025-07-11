def register_prochainfilm(bot):
    bot.add_command('prochainfilm', lambda msg: bot.send_message(msg.chat.id, "🕒 Prochaine publication prévue à 12h00 (film du jour).\nReste connecté !"))
