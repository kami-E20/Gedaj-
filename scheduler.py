import schedule
import time
from datetime import datetime
from scripts.publish import (
    publier_actu_privee, publier_film, publier_quiz,
    publier_correction, sauvegarder_donnees,
    envoyer_statistiques, publier_meilleurs_abonnes,
    publier_abonnes_du_mois
)

def lancer_planification(bot):
    schedule.every().day.at("09:00").do(publier_actu_privee, bot=bot)
    schedule.every().day.at("12:00").do(publier_film, bot=bot)
    schedule.every().day.at("15:00").do(publier_quiz, bot=bot)
    schedule.every().day.at("23:00").do(publier_correction, bot=bot)
    schedule.every().day.at("23:59").do(sauvegarder_donnees, bot=bot)

    schedule.every().sunday.at("18:00").do(envoyer_statistiques, bot=bot)
    schedule.every().sunday.at("20:00").do(publier_meilleurs_abonnes, bot=bot)
    schedule.every().day.at("00:01").do(verifier_debut_mois, bot=bot)

def verifier_debut_mois(bot):
    if datetime.now().day == 1:
        publier_abonnes_du_mois(bot)

def boucle_schedule():
    while True:
        schedule.run_pending()
        time.sleep(20)