import shutil
import datetime

def backup_donnees(bot=None):
    date_str = datetime.datetime.now().strftime('%Y-%m-%d')
    try:
        shutil.copy('data/users.json', f'backup/users_{date_str}.json')
        shutil.copy('data/ranking.json', f'backup/ranking_{date_str}.json')
        shutil.copy('data/reaction_logs.json', f'backup/reaction_logs_{date_str}.json')
        print("✅ Données sauvegardées avec succès.")
    except Exception as e:
        print("❌ Erreur de sauvegarde :", e)