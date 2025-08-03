def register_text_listener(bot):
    from telebot.types import Message
    import random

    # 🤖 Liste d'interactions possibles (aléatoire pour éviter la monotonie)
    SALUTATIONS = [
        "Salut {name} 👋 ! Que puis-je faire pour toi ?",
        "Hey {name} ! Content de te revoir 😊",
        "Bonjour {name}, prêt pour une nouvelle aventure geek ? 🎬"
    ]

    REP_MERCI = [
        "Avec plaisir 💙",
        "Je suis là pour toi !",
        "Toujours dispo 😉"
    ]

    REP_COMPLIMENT = [
        "Tu vas me faire buguer avec tant de compliments 😌",
        "🥹 Merci, t'es adorable !",
        "Je vais rougir... enfin, si j’avais un visage 😅"
    ]

    # Ne réagit qu’aux messages textuels sans "/"
    @bot.message_handler(func=lambda m: m.text and not m.text.startswith('/'))
    def handle_text(message: Message):
        text = message.text.lower()
        user_id = str(message.from_user.id)
        username = message.from_user.username or ""
        first_name = message.from_user.first_name or "Toi"

        # 🎯 Ne répondre que si le message parle à Gedaj
        if not ("gedaj" in text or (message.reply_to_message and message.reply_to_message.from_user.username == "GedajBot")):
            return

        # ✨ Réponses personnalisées
        if any(greeting in text for greeting in ["bonjour", "salut", "hello", "yo", "hey"]):
            bot.send_message(message.chat.id, random.choice(SALUTATIONS).format(name=first_name))

        elif "comment tu vas" in text or "ça va" in text:
            bot.send_message(message.chat.id, f"Je vais super bien {first_name} 😁 Et toi ?")

        elif "merci" in text:
            bot.send_message(message.chat.id, random.choice(REP_MERCI))

        elif "gedaj tu es beau" in text or "tu es mignon" in text or "t'es trop cute" in text:
            bot.send_message(message.chat.id, "🥰 Merci beaucoup ! Toi aussi tu déchires !")

        elif any(word in text for word in ["gentil", "le meilleur", "adorable", "intelligent"]):
            bot.send_message(message.chat.id, random.choice(REP_COMPLIMENT))

        elif "tu es un bot" in text or "tu es un robot" in text:
            bot.send_message(message.chat.id, "Oui 🤖 Mais un bot qui kiffe le cinéma, les quiz et les geeks !")

        elif "gedaj tu peux" in text or "gedaj sais-tu" in text:
            bot.send_message(message.chat.id, "Tu peux taper /help pour découvrir mes super-pouvoirs 🦾")

        elif "gedaj" in text and "aide" in text:
            bot.send_message(message.chat.id, "Besoin d'aide ? Tape simplement /help ou pose ta question directement 😊")

        elif text.startswith("gedaj"):
            if user_id == "879386491":
                bot.send_message(message.chat.id, "Oui papa 😇 Une demande spéciale ?")
            elif user_id == "5618445554":
                bot.send_message(message.chat.id, "Oui tonton 🙏 Toujours dispo pour toi !")
            else:
                bot.send_message(message.chat.id, "Je suis là ! N'hésite pas à taper /help pour voir ce que je sais faire 🎮")

        else:
            # Dernier recours : réponse fun par défaut
            bot.send_message(message.chat.id, "Je suis là 👀 Tu peux me parler ou utiliser une commande comme /help 😉")