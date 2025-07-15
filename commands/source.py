def register_source(bot):
    @bot.message_handler(commands=['source'])
    def handle_source(message):
        texte = (
            "📚 *Sources de Geekmania*\n\n"
            "Toutes les actualités, images et contenus partagés par Geekmania proviennent de sources fiables et vérifiées :\n\n"
            "• Sites officiels des studios (Marvel, Pixar, DC, etc.)\n"
            "• Plateformes de streaming (Netflix, Disney+, Prime Video...)\n"
            "• Bases de données : IMDb, TMDb, AniList, MyAnimeList\n"
            "• Médias spécialisés : Deadline, Variety, AlloCiné, etc.\n\n"
            "🔬 Geekmania s'engage à toujours mentionner ses sources pour garantir la transparence, la crédibilité et le respect scientifique."
        )
        bot.send_message(message.chat.id, texte, parse_mode="Markdown")