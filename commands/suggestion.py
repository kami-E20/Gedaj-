ADMIN_IDS = [879386491, 5618445554]  # Kâmį et Anthony

def register_suggestion(bot):
    @bot.message_handler(commands=['suggestion'])
    def handle_suggestion(message):
        msg = bot.send_message(message.chat.id, "💡 Envoie ta suggestion maintenant :")
        bot.register_next_step_handler(msg, process_suggestion)

    def process_suggestion(message):
        bot.reply_to(message, "Merci pour ta suggestion ! 🙏 Elle a été transmise aux admins.")
        for admin_id in ADMIN_IDS:
            bot.send_message(
                admin_id,
                f"📨 Nouvelle suggestion de {message.from_user.first_name} (ID: {message.from_user.id})\n\n{message.text}"
            )
        from scripts.points import ajouter_points
        ajouter_points(message.from_user.id, "commentaire")