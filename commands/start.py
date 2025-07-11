def register_start(bot):
    bot.add_command('start', lambda msg: bot.send_message(msg.chat.id, "Bienvenue sur 🤖 *Gedaj*, l’assistant officiel de GEEKMANIA !\n\n🎬 Chaque jour : films, quiz, défis, actus...\n📌 Clique sur /help pour tout découvrir.\n👉 Rejoins le canal : https://t.me/GEEKMANIA"))
