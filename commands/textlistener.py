def register_text_listener(bot):
    from telebot.types import Message

    @bot.message_handler(func=lambda m: True)
    def handle_text(message: Message):
        text = message.text.lower()
        user_id = str(message.from_user.id)
        username = message.from_user.username or ""
        first_name = message.from_user.first_name or "Toi"

        # Ignorer les messages non adressés à Gedaj
        if not ("gedaj" in text or message.reply_to_message and message.reply_to_message.from_user.username == "GedajBot"):
            return

        if any(greeting in text for greeting in ["bonjour", "salut", "hello"]):
            bot.send_message(message.chat.id, f"Salut {first_name} 👋 ! Comment puis-je t’aider ?")

        elif "comment tu vas" in text:
            bot.send_message(message.chat.id, "Je vais bien, merci ! Et toi ? 😊")

        elif "merci" in text:
            bot.send_message(message.chat.id, "Je t’en prie, je suis à ton service 💙")

        elif "le meilleur" in text:
            bot.send_message(message.chat.id, "Tes compliments me vont droit au processeur 😌")

        elif "gedaj tu es beau" in text:
            bot.send_message(message.chat.id, "Merci 🥰 Je rougis même si je suis un bot !")

        elif "adorable" in text:
            bot.send_message(message.chat.id, "🥹 Merci, tu es gentil aussi !")

        elif "gedaj tu es un robot" in text or "tu es un bot" in text:
            bot.send_message(message.chat.id, "Oui ! Un assistant geek 🤖 qui adore le cinéma, les quiz et les fans.")

        elif "gedaj tu peux" in text:
            bot.send_message(message.chat.id, "Tape /help pour voir tout ce que je sais faire 🎮")

        elif text.startswith("gedaj"):
            if user_id == "879386491":
                bot.send_message(message.chat.id, "Oui papa 😇")
            elif user_id == "5618445554":
                bot.send_message(message.chat.id, "Oui tonton 🙏")
            else:
                bot.send_message(message.chat.id, "Présent et toujours disponible ! Tape /help 🎬")

        else:
            bot.send_message(message.chat.id, "Je suis là ! Tu peux utiliser une commande ou m’écrire gentiment 😉")