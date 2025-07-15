# commands_admin/admin.py

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

def register_admin(bot):

    @bot.message_handler(commands=['admin'])
    @admin_only
    def handle_admin(message: Message):
        bot.send_message(
            message.chat.id,
            "🔐 *Panneau de commande administrateur - GEDAJ*\n\n"
            "Voici les commandes disponibles pour la gestion du bot :\n\n"
            "🛠️ /adminpanel – Accès au panneau de gestion\n"
            "📛 /lockdown – Verrouiller temporairement les commandes\n"
            "🎬 /forcefilm – Forcer l’envoi d’un film du jour\n"
            "❓ /forcequiz – Forcer l’envoi d’un quiz cinéma\n"
            "📰 /forcenews – Publier manuellement une actu\n"
            "🧪 /test – Tester les fonctionnalités critiques\n"
            "📥 /restorebackup – Restaurer les sauvegardes\n"
            "🪪 /call – Envoyer un appel aux membres\n"
            "🧾 /senddebug – Recevoir les logs de debug du système\n\n"
            "👥 *Réservé aux administrateurs uniquement*",
            parse_mode="Markdown"
        )