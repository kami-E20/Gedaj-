def register_help(bot):
    @bot.message_handler(commands=['help'])
    def handle_help(message):
        bot.send_message(
            message.chat.id,
            "ℹ️ *Voici les commandes disponibles sur Gedaj :*\n\n"
            "🎬 `/filmdujour` – Découvre le film ou l'animation du jour\n"
            "❓ `/quiz` – Tente le quiz du jour et teste tes connaissances\n"
            "📖 `/correction` – Reçois les bonnes réponses du quiz\n"
            "💡 `/suggestion` – Propose un film, une série ou un manga\n"
            "❤️ `/avis` – Donne ton avis sur un contenu publié\n"
            "🏆 `/classement` – Consulte le classement des membres actifs\n"
            "🎭 `/fanpass` – Découvre ton rôle dans la communauté\n"
            "🔐 `/spoiler` – Active le mode anti-spoiler pour éviter les fuites\n"
            "🌐 `/translate` – Traduis un message en anglais ou en français\n"
            "🗣️ `/lang` – Choisis ta langue préférée\n"
            "👥 `/inviter` – Invite un ami et gagne des points\n"
            "📅 `/abodumois` – Découvre l’abonné du mois\n"
            "🔭 `/prochainfilm` – Découvre ce qui arrive bientôt\n"
            "👓 `/vision` – Gère tes préférences de contenu\n"
            "🎯 `/defi` – Reçois un défi cinéphile du jour\n"
            "📚 `/source` – Consulte les sources officielles des actus\n"
            "🎁 `/recompenses` – Découvre les récompenses disponibles"
        , parse_mode="Markdown")