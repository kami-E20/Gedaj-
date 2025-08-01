def register_vision(bot):
    @bot.message_handler(commands=['vision'])
    def handle_vision(message):
        texte = (
            "🎥 *Notre Vision chez Geekmania :*\n\n"
            "Créer la meilleure communauté de passionnés de cinéma, d’animation et de pop culture 🎬✨\n\n"
            "Chaque jour, nous te proposons :\n"
            "• Des films à découvrir\n"
            "• Des quiz ludiques\n"
            "• Des défis originaux\n"
            "• Des classements et récompenses\n\n"
            "Rejoins-nous dans cette aventure geek, et montre que tu es un vrai fan ! ❤️👾"
        )
        bot.send_message(message.chat.id, texte, parse_mode="Markdown")