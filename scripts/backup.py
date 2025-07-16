import shutil
import datetime
import os

def backup_donnees(bot=None):
    date_str = datetime.datetime.now().strftime('%Y-%m-%d')

    FILES_TO_BACKUP = {
        "data/users.json": f"backup/users_{date_str}.json",
        "data/ranking.json": f"backup/ranking_{date_str}.json",
        "data/reaction_logs.json": f"backup/reaction_logs_{date_str}.json"
    }

    os.makedirs("backup", exist_ok=True)

    try:
        for src, dest in FILES_TO_BACKUP.items():
            if os.path.exists(src):
                shutil.copy(src, dest)
        print("✅ Données sauvegardées avec succès.")
        if bot:
            bot.send_message(
                os.getenv("ADMIN_DEFAULT", "879386491"),
                f"💾 Sauvegarde automatique terminée avec succès ({date_str})"
            )
    except Exception as e:
        print("❌ Erreur de sauvegarde :", e)
        if bot:
            bot.send_message(
                os.getenv("ADMIN_DEFAULT", "879386491"),
                f"❌ Erreur lors de la sauvegarde automatique : {e}"
            )