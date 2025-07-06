def register_recompenses(bot):
    @bot.message_handler(commands=['recompenses'])
    def handle(message):
        msg = (
            "🎁 Récompenses Geekmania :\n\n"
            "🏅 1er : Poster personnalisé + badge FanPass\n"
            "🥈 2ème : Film au choix en avant-première\n"
            "🥉 3 à 5 : Mention spéciale + rôle VIP\n"
            "\nLes classements sont mis à jour chaque dimanche soir !"
        )
        bot.reply_to(message, msg)