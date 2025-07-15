def register_vision(bot):
    @bot.message_handler(commands=['vision'])
    def handle_vision(message):
        texte = (
            "🎯 *Vision de Geekmania*\n\n"
            "Geekmania a pour mission de rassembler tous les passionnés de cinéma, séries, et animations\n"
            "autour d’une communauté active, bienveillante et passionnée.\n\n"
            "🌟 Nous voulons créer un espace où chacun peut :\n"
            "• Découvrir des films et animations de qualité 🎬\n"
            "• Tester ses connaissances avec des quiz ludiques 🧠\n"
            "• Partager ses avis et suggestions 🗣️\n"
            "• Participer à des défis et concours réguliers 🏆\n\n"
            "🚀 Rejoins-nous pour vivre cette aventure geek unique et enrichissante !"
        )
        bot.send_message(message.chat.id, texte, parse_mode="Markdown")
