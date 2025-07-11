
import schedule
import time
import threading
import subprocess

def run_script(path):
    try:
        subprocess.run(["python", path], check=True)
    except Exception as e:
        print(f"Erreur lors de l'exécution de {path} :", e)

def schedule_tasks():
    # ⏰ 09h00 - Actualités privées aux admins (anilist + RSS)
    schedule.every().day.at("09:00").do(run_script, path="scripts/notify_blocks.py")

    # ⏰ 12h00 - Film du jour
    schedule.every().day.at("12:00").do(run_script, path="scripts/publish.py")

    # ⏰ 15h00 - Quiz du jour
    schedule.every().day.at("15:00").do(run_script, path="scripts/generate_quiz_message.py")

    # ⏰ 23h00 - Correction du quiz
    schedule.every().day.at("23:00").do(run_script, path="scripts/correction.py")

    # ⏰ 23h59 - Sauvegarde des données
    schedule.every().day.at("23:59").do(run_script, path="scripts/backup.py")

    # ⏰ Dimanche 18h - Statistiques hebdo
    schedule.every().sunday.at("18:00").do(run_script, path="scripts/stats.py")

    # ⏰ Dimanche 20h - Top abonnés de la semaine
    schedule.every().sunday.at("20:00").do(run_script, path="scripts/top_weekly.py")

def run_scheduler():
    schedule_tasks()
    while True:
        schedule.run_pending()
        time.sleep(1)

def start():
    threading.Thread(target=run_scheduler).start()
