def register_filmdujour(bot):
    bot.add_command('filmdujour', lambda msg: bot.send_message(msg.chat.id, "🎬 Voici le *film ou l’animation du jour* !\nRéagis avec ❤️ ou 👍 pour débloquer plus !"))
