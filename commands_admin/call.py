from telebot import TeleBot

AUTHORIZED_ADMINS = [5618445554, 879386491]

def register_call(bot: TeleBot):
    @bot.message_handler(commands=['call'])
    def handle_call(message):
        text = (
            "📞 *Besoin d’aide ?*\n\n"
            "L’équipe admin a été notifiée. Tu peux aussi utiliser /suggestion ou /avis pour nous faire part d’un problème ou d’une idée."
        )
        bot.send_message(message.chat.id, text, parse_mode="Markdown")

        for admin_id in AUTHORIZED_ADMINS:
            bot.send_message(admin_id, f"📬 L'utilisateur {message.from_user.first_name} (@{message.from_user.username}) a utilisé /call.")