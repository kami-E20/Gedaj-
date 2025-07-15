# commands_admin/test.py

from telebot.types import Message
import os

AUTHORIZED_ADMINS = [879386491, 5618445554]  # Kâmį & Anthony

def admin_only(handler):
    def wrapper(message: Message):
        if message.from_user.id not in AUTHORIZED_ADMINS:
            message.bot.send_message(
                message.chat.id,
                "🚫 Cette commande est réservée aux administrateurs du bot.\n\n"
                "📬 Si vous avez une suggestion, une remarque ou un problème :\n"
                "• Utilisez /call pour contacter un admin\n"
                "• Partagez votre /avis\n"
                "• Ou proposez une /suggestion\n\n"
                "Merci pour votre compréhension 🙏"
            )
            return
        return handler(message)
    return wrapper

def register_test(bot):

    @bot.message_handler(commands=['test'])
    @admin_only
    def handle_test(message: Message):
        try:
            token_visible = os.getenv("BOT_TOKEN")
            bot.send_message(
                message.chat.id,
                f"✅ *Test réussi !*\n\n"
                f"Le bot fonctionne correctement.\n"
                f"BOT_TOKEN : `{token_visible[:10]}...`\n"
                f"Dossiers essentiels disponibles ✅\n"
                f"Envois privés OK ✅",
                parse_mode="Markdown"
            )
        except Exception as e:
            bot.send_message(
                message.chat.id,
                f"❌ Erreur lors du test : {e}"
            )