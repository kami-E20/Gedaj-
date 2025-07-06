import schedule
import time
from scripts.backup import backup_donnees
from scripts.points import publier_meilleurs_abonnes, publier_abonnes_du_mois
from datetime import datetime

def run_scheduler():
    schedule.every().day.at("23:59").do(backup_donnees)
    schedule.every().sunday.at("20:00").do(publier_meilleurs_abonnes)
    schedule.every().day.at("00:01").do(verifier_debut_mois)

    while True:
        schedule.run_pending()
        time.sleep(1)

def verifier_debut_mois():
    if datetime.now().day == 1:
        publier_abonnes_du_mois()