import os
from telebot import TeleBot
from apscheduler.schedulers.background import BackgroundScheduler
from pytz import timezone
from datetime import datetime
from scripts import publish

def main():
    # Charger le token depuis variable d'environnement
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    if not TOKEN:
        print("❌ TELEGRAM_BOT_TOKEN non défini !")
        return

    bot = TeleBot(TOKEN)

    # Configurer scheduler avec timezone Kinshasa
    sched = BackgroundScheduler(timezone=timezone("Africa/Kinshasa"))

    # Jobs planifiés à 09:00 tous les jours
    sched.add_job(publish.publier_actu_privee, 'cron', hour=9, minute=0, args=[bot])
    sched.add_job(publish.publier_film, 'cron', hour=9, minute=0, args=[bot])
    sched.add_job(publish.publier_quiz, 'cron', hour=9, minute=0, args=[bot])
    sched.add_job(publish.publier_correction, 'cron', hour=9, minute=5, args=[bot])  # correction un peu après quiz
    sched.add_job(publish.sauvegarder_donnees, 'cron', hour=23, minute=55, args=[bot])  # sauvegarde la nuit

    # Autres publications à horaires spécifiques (exemple hebdomadaire dimanche 20h)
    sched.add_job(publish.envoyer_statistiques, 'cron', day_of_week='sun', hour=20, minute=0, args=[bot])
    sched.add_job(publish.publier_meilleurs_abonnes, 'cron', day_of_week='sun', hour=20, minute=15, args=[bot])
    sched.add_job(publish.publier_abonnes_du_mois, 'cron', day=1, hour=10, minute=0, args=[bot])  # 1er du mois

    sched.start()
    print("✅ Scheduler démarré, publications planifiées")

    # Pour garder le programme vivant
    bot.infinity_polling()

if __name__ == "__main__":
    main()