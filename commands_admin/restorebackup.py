# restore_backup.py
import os
import shutil
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

# Admins autorisés
ADMIN_IDS = [5618445554, 879386491]

# Dossiers
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
BACKUP_DIR = os.path.join(PROJECT_ROOT, "backups")

# Correspondance fichiers backup → fichiers réels
BACKUP_FILES = {
    "ranking_backup.json": "ranking.json",
    "reaction_logs_backup.json": "reaction_logs.json",
    "users_backup.json": "users.json"
}

def restore_backup(update: Update, context: CallbackContext):
    user_id = update.effective_user.id

    # Vérif admin
    if user_id not in ADMIN_IDS:
        update.message.reply_text("⛔ Vous n’êtes pas autorisé à restaurer une sauvegarde.")
        return

    restored_count = 0

    try:
        for backup_name, target_name in BACKUP_FILES.items():
            backup_path = os.path.join(BACKUP_DIR, backup_name)
            target_path = os.path.join(DATA_DIR, target_name)

            if os.path.exists(backup_path):
                shutil.copy2(backup_path, target_path)
                restored_count += 1

        if restored_count > 0:
            update.message.reply_text(f"✅ {restored_count} fichiers restaurés depuis les sauvegardes.")
        else:
            update.message.reply_text("⚠️ Aucun fichier de sauvegarde trouvé dans backups/.")

        # Notifier les autres admins
        for admin_id in ADMIN_IDS:
            if admin_id != user_id:
                context.bot.send_message(
                    chat_id=admin_id,
                    text=f"ℹ️ {update.effective_user.first_name} a restauré {restored_count} fichiers depuis backups/"
                )

    except Exception as e:
        update.message.reply_text(f"❌ Erreur lors de la restauration : {str(e)}")

# Handler
restore_backup_handler = CommandHandler("restore_backup", restore_backup)