def register_correction(bot):
    @bot.message_handler(commands=['correction'])
    def handle_correction(message):
        bot.send_message(
            message.chat.id,
            "🧐 *Voici la correction du quiz d’aujourd’hui :*\n\n"
            "📌 Les bonnes réponses s’affichent ici automatiquement après ta participation.\n"
            "🧠 Continue de jouer chaque jour pour améliorer ton score !",
            parse_mode="Markdown"
        )