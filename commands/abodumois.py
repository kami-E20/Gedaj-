def register_abodumois(bot):
    @bot.message_handler(commands=['abodumois'])
    def handle(message):
        msg = (
            "👑 L'abonné du mois est désigné parmi les 5 meilleurs chaque semaine.\n\n"
            "Les critères sont :\n"
            "- Interactions régulières (likes, quiz, commentaires)\n"
            "- Suggestions pertinentes\n"
            "- Esprit communautaire\n"
            "\nBonne chance à tous !"
        )
        bot.reply_to(message, msg)