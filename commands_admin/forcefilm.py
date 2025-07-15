# commands_admin/forcefilm.py

from telebot.types import Message
from scripts import publish  # Importer le module publish

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

def register_forcefilm(bot):

    @bot.message_handler(commands=['forcefilm'])
    @admin_only
    def handle_forcefilm(message: Message):
        try:
            publish.publish_film_du_jour(bot)
            bot.send_message(message.chat.id, "🎬 Forçage du film du jour exécuté avec succès.")
        except Exception as e:
            bot.send_message(message.chat.id, f"❌ Erreur lors du forçage : {e}")