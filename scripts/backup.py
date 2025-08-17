# backup.py
import datetime
import shutil
import os

def backup_donnees(bot=None):
    date_str = datetime.datetime.now().strftime('%Y-%m-%d')

    DATA_DIR = "data"
    BACKUP_DIR = "backup"

    os.makedirs(BACKUP_DIR, exist_ok=True)

    FILES = {
        "users.json": "users",
        "ranking.json": "ranking",
        "reaction_logs.json": "reaction_logs"
    }

    try:
        for file_name, base_name in FILES.items():
            source = os.path.join(DATA_DIR, file_name)

            if os.path.exists(source):
                # Sauvegarde datée
                dated_backup = os.path.join(BACKUP_DIR, f"{base_name}_{date_str}.json")
                shutil.copy(source, dated_backup)

                # Sauvegarde fixe
                fixed_backup = os.path.join(BACKUP_DIR, f"{base_name}_backup.json")
                shutil.copy(source, fixed_backup)

        print("✅ Données sauvegardées avec succès (datées + fixes).")

    except Exception as e:
        print("❌ Erreur de sauvegarde :", e)