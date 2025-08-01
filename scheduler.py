from datetime import datetime
from time import sleep
from loader import bot
from scripts.publish import (
    publier_film,
    publier_quiz,
    publier_correction,
    publier_actu_privee,
    envoyer_statistiques,
    publier_meilleurs_abonnes,
    publier_abonnes_du_mois,
    sauvegarder_donnees,
)
from scripts.backup import backup_donnees

def lancer_taches_scheduled():
    print("⏱️ Planificateur en marche...")

    while True:
        now = datetime.now()

        heure = now.strftime("%H:%M")

        try:
            # 🕘 Tous les jours à 09h00
            if heure == "09:00":
                publier_film(bot)
                publier_quiz(bot)
                publier_actu_privee(bot)

            # 🕒 Tous les jours à 15h00
            if heure == "15:00":
                publier_correction(bot)

            # 🕙 Tous les jours à 22h00 : sauvegarde + backup
            if heure == "22:00":
                sauvegarder_donnees(bot)
                backup_donnees(bot)

            # 📊 Chaque dimanche à 20h00
            if now.weekday() == 6 and heure == "20:00":
                envoyer_statistiques(bot)
                publier_meilleurs_abonnes(bot)

            # 🎁 Le 1er jour de chaque mois à 10h00
            if now.day == 1 and heure == "10:00":
                publier_abonnes_du_mois(bot)

        except Exception as e:
            print("❌ Erreur dans une tâche programmée :", e)

        sleep(60)  # ⏳ Vérifie chaque minute