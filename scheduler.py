import schedule
import time
from datetime import datetime
from scripts.fetch_anilist_news import fetch_anilist_news
from scripts.fetch_cinema_news import fetch_cinema_news
from scripts.fetch_anime_rss import fetch_anime_rss
from scripts.admin_notify import send_admin_news
from scripts.backup import backup_donnees
from scripts.points import publier_meilleurs_abonnes, publier_abonnes_du_mois

def envoyer_actus_du_jour():
    from main import bot
    anime = fetch_anilist_news()
    cinema = fetch_cinema_news()
    rss = fetch_anime_rss()
    if anime:
        send_admin_news(bot, anime, categorie="Anime (AniList)")
    if cinema:
        send_admin_news(bot, cinema, categorie="Cinéma")
    if rss:
        send_admin_news(bot, rss, categorie="Anime (RSS)")

def verifier_debut_mois():
    if datetime.now().day == 1:
        publier_abonnes_du_mois()

def run_scheduler():
    schedule.every().day.at("09:00").do(envoyer_actus_du_jour)
    schedule.every().day.at("23:59").do(backup_donnees)
    schedule.every().sunday.at("20:00").do(publier_meilleurs_abonnes)
    schedule.every().day.at("00:01").do(verifier_debut_mois)

    while True:
        schedule.run_pending()
        time.sleep(1)