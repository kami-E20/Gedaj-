ADMIN_IDS = [879386491, 5618445554]

def register_avis(bot):
    @bot.message_handler(commands=['avis'])
    def handle_avis(message):
        msg = bot.send_message(message.chat.id, "📝 Envoie ton avis sur le contenu du jour :")
        bot.register_next_step_handler(msg, process_avis)

    def process_avis(message):
        bot.reply_to(message, "Merci pour ton retour ! 🧠 Les admins vont le consulter.")
        for admin_id in ADMIN_IDS:
            bot.send_message(
                admin_id,
                f"🗣️ Nouvel avis de {message.from_user.first_name} (ID: {message.from_user.id})\n\n{message.text}"
            )
        from scripts.points import ajouter_points
        ajouter_points(message.from_user.id, "commentaire")