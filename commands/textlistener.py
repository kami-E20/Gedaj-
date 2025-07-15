from telebot.types import Message

ADMIN_IDS = {
    5618445554: "Anthony",
    879386491: "Kami"
}

def register_text_listener(bot):

    @bot.message_handler(func=lambda m: True, content_types=['text'])
    def handle_text(message: Message):
        text = message.text.lower().strip()
        user_id = message.from_user.id
        username = message.from_user.username or message.from_user.first_name or "utilisateur"

        # Ignore les commandes
        if text.startswith('/'):
            return

        # Condition : ne répondre que si "gedaj" est mentionné dans le texte
        # OU si c'est une réponse à un message du bot lui-même
        is_addressed_to_gedaj = "gedaj" in text
        is_reply_to_gedaj = message.reply_to_message and message.reply_to_message.from_user and message.reply_to_message.from_user.is_bot

        if not (is_addressed_to_gedaj or is_reply_to_gedaj):
            return  # Ignore tout autre message

        # Mots/phrases ciblés avec réponses personnalisées
        if text in ["bonjour gedaj", "bonjour"]:
            bot.reply_to(message, "👋 Bonjour ! Je suis Gedaj, ravi de te retrouver.")
            return

        if text in ["comment vas-tu gedaj", "je vais bien et toi?"]:
            bot.reply_to(message, "😊 Je vais très bien, merci ! Et toi ?")
            return

        if text in ["merci gedaj"]:
            bot.reply_to(message, "🙏 Je t'en prie, je suis à ton service.")
            return

        if text in ["tu es le meilleur gedaj"]:
            bot.reply_to(message, "😊 Tes compliments me flattent, merci beaucoup !")
            return

        if text.startswith("gedaj tu peux"):
            bot.reply_to(message, "👉 Tape /help pour découvrir tout ce que je peux faire !")
            return

        if text in ["gedaj tu es beau"]:
            bot.reply_to(message, "😊 Merci, ça me fait plaisir !")
            return

        if text in ["gedaj tu es un robot"]:
            bot.reply_to(message, "🤖 Je suis un bot intelligent conçu pour t’aider avec tout ce qui concerne le cinéma, les séries et plus encore !")
            return

        if text in ["gedaj tu es adorable"]:
            bot.reply_to(message, "😊🥰")  # Emoji rougis
            return

        if text.startswith("gedaj"):
            if user_id in ADMIN_IDS:
                if ADMIN_IDS[user_id] == "Kami":
                    bot.reply_to(message, "Oui papa 👑")
                elif ADMIN_IDS[user_id] == "Anthony":
                    bot.reply_to(message, "Oui tonton 👋")
                else:
                    bot.reply_to(message, "Présent et toujours disponible ! Tape /help pour voir mes fonctionnalités.")
            else:
                bot.reply_to(message, "Présent et toujours disponible ! Tape /help pour voir mes fonctionnalités.")
            return

        # Réponses génériques à quelques salutations courtes
        salutations = ["salut", "hello", "coucou"]
        if any(s in text for s in salutations):
            bot.reply_to(message, f"👋 Salut {username}! Tape /help pour découvrir mes commandes.")
            return

        # Merci générique
        if "merci" in text:
            bot.reply_to(message, "🙏 Avec plaisir !")
            return