def register_filmdujour(bot):
    @bot.message_handler(commands=['filmdujour'])
    def handle_filmdujour(message):
        bot.send_message(
            message.chat.id,
            "🎬 *Film du jour !*\n\n"
            "Chaque jour, découvre une pépite du cinéma ou de l’animation sélectionnée rien que pour toi.\n"
            "❤️ Réagis au message pour débloquer le lien de téléchargement quand la communauté atteint le quota !\n\n"
            "👉 Le film va s'afficher dans quelques instants...",
            parse_mode="Markdown"
        )
        # L’envoi du film (affiche, synopsis, etc.) sera déclenché par une autre fonction dédiée