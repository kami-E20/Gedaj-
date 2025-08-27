import os
import shutil
import telebot

# Token du bot (tu l'importes depuis ta config si nécessaire)
from config import BOT_TOKEN  

bot = telebot.TeleBot(BOT_TOKEN)

# Admins autorisés
ADMIN_IDS = [5618445554, 879386491]

# Dossiers
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
BACKUP_DIR = os.path.join(PROJECT_ROOT, "backup")

# Correspondance fichiers backup → fichiers réels
BACKUP_FILES = {
    "ranking_backup.json": "ranking.json",
    "reaction_logs_backup.json": "reaction_logs.json",
    "users_backup.json": "users.json"
}

# Commande admin pour restaurer les backups
@bot.message_handler(commands=["restore_backup"])
def restore_backup(message):
    user_id = message.from_user.id

    # Vérification admin
    if user_id not in ADMIN_IDS:
        bot.reply_to(message, "⛔ Vous n’êtes pas autorisé à restaurer une sauvegarde.")
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
            bot.reply_to(message, f"✅ {restored_count} fichiers restaurés depuis les sauvegardes.")
        else:
            bot.reply_to(message, "⚠️ Aucun fichier de sauvegarde trouvé dans backups/.")

        # Notifier les autres admins
        for admin_id in ADMIN_IDS:
            if admin_id != user_id:
                bot.send_message(
                    admin_id,
                    f"ℹ️ {message.from_user.first_name} a restauré {restored_count} fichiers depuis backups/"
                )

    except Exception as e:
        bot.reply_to(message, f"❌ Erreur lors de la restauration : {str(e)}")