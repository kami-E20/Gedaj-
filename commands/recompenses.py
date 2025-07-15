def register_recompenses(bot):
    @bot.message_handler(commands=['recompenses'])
    def handle_recompenses(message):
        texte = (
            "🏆 *Récompenses Geekmania – Système de Points*\n\n"
            "🎯 Gagne des points en participant aux activités : quiz, défis, suggestions, réactions, etc.\n\n"
            "📈 *Paliers de récompenses :*\n"
            "• 🥉 50 pts — Fan confirmé (badge symbolique)\n"
            "• 🥈 100 pts — Accès prioritaire aux contenus bonus\n"
            "• 🥇 200 pts — Membre VIP (contenus exclusifs, rôle spécial)\n"
            "• 👑 500 pts — Ambassadeur Geekmania (mention d'honneur)\n\n"
            "🔍 Utilise /classement pour voir ta position\n"
            "📢 Et continue à participer pour débloquer tous les niveaux !"
        )
        bot.send_message(message.chat.id, texte, parse_mode="Markdown")