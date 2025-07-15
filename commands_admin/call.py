# commands_admin/call.py

from telebot.types import Message

ADMIN_IDS = [879386491, 5618445554]  # Kâmį & Anthony

def register_call(bot):

    @bot.message_handler(commands=['call'])
    def handle_call(message: Message):
        user = message.from_user
        username = f"@{user.username}" if user.username else "Utilisateur sans username"
        user_message = message.text.replace('/call', '').strip()

        if not user_message:
            user_message = "❓ Aucun message fourni."

        notification = (
            f"📞 *Appel d'un abonné !*\n\n"
            f"👤 *Nom :* {user.first_name} {user.last_name or ''}\n"
            f"🔗 *Username :* {username}\n"
            f"🆔 *ID :* `{user.id}`\n\n"
            f"🗣 *Message :*\n_{user_message}_"
        )

        # Envoie aux admins
        for admin_id in ADMIN_IDS:
            try:
                bot.send_message(admin_id, notification, parse_mode="Markdown")
            except Exception as e:
                print(f"Erreur en envoyant à l'admin {admin_id} : {e}")

        # Confirmation à l'utilisateur
        bot.send_message(
            message.chat.id,
            "📨 Votre message a été transmis aux administrateurs. Ils vous répondront bientôt. Merci !"
        )