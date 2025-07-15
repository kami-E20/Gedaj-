# commands_admin/adminpanel.py

from telebot.types import Message

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

def register_adminpanel(bot):

    @bot.message_handler(commands=['adminpanel'])
    @admin_only
    def handle_adminpanel(message: Message):
        bot.send_message(
            message.chat.id,
            "📊 *Panel Administrateur – GEDAJ*\n\n"
            "Bienvenue dans l’espace de gestion du bot.\n"
            "Tu peux ici piloter les fonctions critiques comme :\n"
            "• Forcer les publications\n"
            "• Restaurer les sauvegardes\n"
            "• Verrouiller ou relancer le bot\n\n"
            "Tape /admin pour voir toutes les commandes disponibles.",
            parse_mode="Markdown"
        )