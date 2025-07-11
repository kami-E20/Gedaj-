def register_correction(bot):
    bot.add_command('correction', lambda msg: bot.send_message(msg.chat.id, "✅ Voici les réponses du *quiz précédent*.\nMerci d’avoir participé, tes points ont été mis à jour !"))
