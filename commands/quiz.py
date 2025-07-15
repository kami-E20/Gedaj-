def register_quiz(bot):
    @bot.message_handler(commands=['quiz'])
    def handle_quiz(message):
        bot.send_message(
            message.chat.id,
            "🎬 *Quiz du jour !*\n\n"
            "Répondez à la question cinéma du jour et gagnez des points 🎯.\n"
            "Vous recevrez la correction après avoir participé !\n\n"
            "📝 Le quiz vous sera envoyé automatiquement. Bonne chance !",
            parse_mode="Markdown"
        )
        # Le vrai quiz peut être lancé ici plus tard avec des boutons ou questions