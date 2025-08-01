def register_help(bot):
    from telebot.types import Message

    @bot.message_handler(commands=['help'])
    def handle_help(message: Message):
        user_id = message.from_user.id
        is_admin = str(user_id) in ["5618445554", "879386491"]  # Anthony et Kâmį

        texte = (
            "🎯 *Commandes Geekmania disponibles :*\n\n"
            "📌 *Utilisateurs :*\n"
            "• /start — Démarrer le bot\n"
            "• /filmdujour — Voir le film recommandé\n"
            "• /quiz — Participer au quiz\n"
            "• /correction — Corriger le quiz d'hier\n"
            "• /fanpass — Voir ton Fan Pass et ton statut\n"
            "• /classement — Top 10 des fans\n"
            "• /abodumois — Voir l’abonné mis à l’honneur\n"
            "• /defi — Le défi hebdo Geekmania\n"
            "• /inviter — Gagne des points en partageant\n"
            "• /avis — Donne ton avis\n"
            "• /suggestion — Propose un film/série\n"
            "• /spoiler — Mode spoiler\n"
            "• /lang — Changer la langue\n"
            "• /call — Contacter l’équipe"

        )

        if is_admin:
            texte += (
                "\n\n🛡️ *Commandes Admin :*\n"
                "• /adminpanel — Voir le panneau admin\n"
                "• /forcefilm — Forcer la publication du film\n"
                "• /forcequiz — Forcer un quiz\n"
                "• /forcenews — Forcer l’actu privée\n"
                "• /lockdown — Activer le mode silence\n"
                "• /senddebug — Envoyer les infos debug\n"
                "• /restorebackup — Restaurer les données\n"
                "• /test — Tester toutes les fonctions\n"
            )

        bot.send_message(message.chat.id, texte, parse_mode="Markdown")