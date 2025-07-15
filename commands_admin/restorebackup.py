# commands_admin/restorebackup.py

from telebot.types import Message
import shutil
import os

AUTHORIZED_ADMINS = [879386491, 5618445554]  # Kâmį & Anthony

DATA_DIR = "data"
BACKUP_DIR = "backup"

FILES_TO_RESTORE = {
    "users_backup.json": "users.json",
    "ranking_backup.json": "ranking.json",
    "reaction_logs_backup.json": "reaction_logs.json"
}

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

def register_restorebackup(bot):

    @bot.message_handler(commands=['restorebackup'])
    @admin_only
    def handle_restorebackup(message: Message):
        try:
            restored = []
            for backup_file, target_file in FILES_TO_RESTORE.items():
                backup_path = os.path.join(BACKUP_DIR, backup_file)
                target_path = os.path.join(DATA_DIR, target_file)
                if os.path.exists(backup_path):
                    shutil.copy2(backup_path, target_path)
                    restored.append(target_file)
            if restored:
                bot.send_message(message.chat.id, f"✅ Restauration terminée pour : {', '.join(restored)}.")
            else:
                bot.send_message(message.chat.id, "⚠️ Aucun fichier de sauvegarde trouvé.")
        except Exception as e:
            bot.send_message(message.chat.id, f"❌ Erreur lors de la restauration : {e}")