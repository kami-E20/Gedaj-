import os
import shutil
from telebot import TeleBot

# ✅ Liste des admins autorisés
AUTHORIZED_ADMINS = [5618445554, 879386491]  # Anthony & Kâmį

# 🔁 Paires de fichiers à restaurer
RESTORE_MAP = {
    "backup/users_backup.json": "data/users.json",
    "backup/ranking_backup.json": "data/ranking.json",
    "backup/reaction_logs_backup.json": "data/reaction_logs.json"
}

def register_restorebackup(bot: TeleBot):
    @bot.message_handler(commands=['restorebackup'])
    def handle_restorebackup(message):
        user_id = message.from_user.id

        # 🔒 Vérification admin
        if user_id not in AUTHORIZED_ADMINS:
            bot.reply_to(message, "⛔ Cette commande est réservée aux administrateurs.\nUtilise /call ou /suggestion pour contacter l’équipe.")
            return

        success_count = 0
        errors = []

        for src, dest in RESTORE_MAP.items():
            if os.path.exists(src):
                try:
                    shutil.copy(src, dest)
                    success_count += 1
                except Exception as e:
                    errors.append(f"❌ Erreur sur {src} → {e}")
            else:
                errors.append(f"⚠️ Fichier de sauvegarde manquant : {src}")

        # ✅ Résumé de l’opération
        if success_count > 0:
            bot.send_message(message.chat.id, f"✅ {success_count} fichiers restaurés avec succès.")
        if errors:
            bot.send_message(message.chat.id, "\n".join(errors))