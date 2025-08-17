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
    publier_anniversaires,
    publier_images_acteurs,
    notifier_admins_daily,
)
from scripts.backup import backup_donnees


def lancer_taches_scheduled():
    print("⏱️ Planificateur en marche...")

    while True:
        now = datetime.now()
        heure = now.strftime("%H:%M")

        try:
            # 🕘 Tous les jours à 09h00 → Film + Quiz + News (AniList + RSS)
            if heure == "09:00":
                publier_film(bot)
                publier_quiz(bot)
                publier_actu_privee(bot)

            # 🕒 Tous les jours à 15h00 → Correction quiz
            if heure == "15:00":
                publier_correction(bot)

            # 🕕 Tous les jours à 18h00 → Anniversaires du jour + anecdote cinéma
            if heure == "18:00":
                publier_anniversaires(bot)

            # 🕖 Tous les jours à 19h00 → Images "acteurs hier vs aujourd’hui"
            if heure == "19:00":
                publier_images_acteurs(bot)

            # 🕙 Tous les jours à 22h00 → Sauvegarde + Backup
            if heure == "22:00":
                sauvegarder_donnees(bot)
                backup_donnees(bot)

            # 🕤 Tous les jours à 21h30 → Message privé aux admins (incitation à interagir)
            if heure == "21:30":
                notifier_admins_daily(bot)

            # 📊 Chaque dimanche à 20h00 → Stats + Top abonnés
            if now.weekday() == 6 and heure == "20:00":
                envoyer_statistiques(bot)
                publier_meilleurs_abonnes(bot)

            # 🎁 Le 1er jour de chaque mois à 10h00 → Abonnés du mois
            if now.day == 1 and heure == "10:00":
                publier_abonnes_du_mois(bot)

        except Exception as e:
            print("❌ Erreur dans une tâche programmée :", e)

        sleep(60)  # ⏳ Vérifie chaque minute