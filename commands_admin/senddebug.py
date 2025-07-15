# commands_admin/senddebug.py

from telebot.types import Message
import os

AUTHORIZED_ADMINS = [879386491, 5618445554]  # Kâmį & Anthony

FILES_TO_SEND = [
    "data/users.json",
    "data/ranking.json",
    "data/reaction_logs.json",
    "backup/users_backup.json",
    "backup/ranking_backup.json",
    "backup/reaction_logs_backup.json"
]

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

def register_senddebug(bot):

    @bot.message_handler(commands=['senddebug'])
    @admin_only
    def handle_senddebug(message: Message):
        try:
            sent_any = False
            for path in FILES_TO_SEND:
                if os.path.exists(path):
                    with open(path, "rb") as f:
                        bot.send_document(message.chat.id, f, caption=f"📄 {os.path.basename(path)}")
                        sent_any = True
            if not sent_any:
                bot.send_message(message.chat.id, "⚠️ Aucun fichier de debug trouvé.")
        except Exception as e:
            bot.send_message(message.chat.id, f"❌ Erreur lors de l’envoi des fichiers debug : {e}")