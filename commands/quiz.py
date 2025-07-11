def register_quiz(bot):
    bot.add_command('quiz', lambda msg: bot.send_message(msg.chat.id, "🎯 Prépare-toi à tester tes connaissances cinéma !\n\nUtilise les boutons pour répondre au quiz du jour."))
