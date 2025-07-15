def register_start(bot):
    @bot.message_handler(commands=['start'])
    def handle_start(message):
        bot.send_message(
            message.chat.id,
            "👋 *Bonjour ! Je suis Gedaj,* votre assistant personnel dédié au monde du cinéma, des séries et de l'animation. 🎬✨\n\n"
            "🎯 Chaque jour, je vous propose :\n"
            "• Le film ou l’animation du jour 🎥\n"
            "• Un quiz exclusif pour tester vos connaissances 🎯\n"
            "• Des actus, anecdotes et classements à ne pas manquer 🗞️\n\n"
            "💬 Pour profiter pleinement de l’expérience, *rejoignez notre communauté Geekmania* : échanges, votes, suggestions et exclusivités vous y attendent !\n"
            "👉 [Accéder au groupe](https://t.me/GEEKMANIA)\n\n"
            "🧭 Utilisez la commande /help pour découvrir tout ce que je peux faire.\n"
            "🚀 Prêt à explorer l’univers Geekmania avec moi ?"
        , parse_mode="Markdown", disable_web_page_preview=True)
