import schedule
import time
from scripts.backup import backup_donnees

def run_scheduler():
    schedule.every().day.at("23:59").do(backup_donnees)

    while True:
        schedule.run_pending()
        time.sleep(1)