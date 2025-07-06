import feedparser
from datetime import datetime, timedelta

def fetch_cinema_sorties():
    # RSS d'allocine - prochaines sorties (à adapter selon région si besoin)
    feed = feedparser.parse("https://www.allocine.fr/rss/films_a_l_affiche.xml")
    target = (datetime.now() + timedelta(days=7)).date()
    result = []

    for entry in feed.entries[:10]:
        title = entry.title
        summary = entry.summary
        link = entry.link
        result.append({
            "titre": title,
            "description": summary,
            "date": target.strftime("%d/%m/%Y"),
            "lien": link
        })

    return result