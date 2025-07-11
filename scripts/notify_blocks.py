
import requests
from telegram import Bot

# Remplace par ton token (ou récupère-le de os.environ)
BOT_TOKEN = "TON_TOKEN_ICI"
bot = Bot(token=BOT_TOKEN)

KAMI_ID = 879386491
ANTHONY_ID = 5618445554

def fetch_anilist_news():
    # Exemple simple d'une actu manga simulée
    return {
        "catégorie": "Animé",
        "titre": "Jujutsu Kaisen Saison 3 Confirmée",
        "résumé": "MAPPA annonce une sortie début 2026 basée sur l'arc Shibuya Incident.",
        "source": "https://anilist.co/news",
        "image_url": "https://example.com/jujutsu.jpg"
    }

def fetch_cinema_news():
    # Exemple simple d'une actu cinéma simulée
    return {
        "catégorie": "Cinéma",
        "titre": "Dune: Partie 3 officiellement annoncée",
        "résumé": "Legendary Pictures confirme une suite prévue pour 2026.",
        "source": "https://rss.cinemanews.com",
        "image_url": "https://example.com/dune.jpg"
    }

def envoyer_actu(actu, admin_id):
    message = f"🎬 [ACTU GEEKMANIA DU JOUR]\n\n🧩 Catégorie : {actu['catégorie']}\n🗞️ Titre : {actu['titre']}\n📌 Résumé : {actu['résumé']}\n🔗 Source : {actu['source']}\n\n🖼️ Image ci-dessous 👇"
    bot.send_message(chat_id=admin_id, text=message)
    if actu['image_url']:
        bot.send_photo(chat_id=admin_id, photo=actu['image_url'])

def envoyer_actualites():
    anime = fetch_anilist_news()
    cinema = fetch_cinema_news()

    for admin_id in [KAMI_ID, ANTHONY_ID]:
        envoyer_actu(anime, admin_id)
        envoyer_actu(cinema, admin_id)

if __name__ == "__main__":
    envoyer_actualites()
