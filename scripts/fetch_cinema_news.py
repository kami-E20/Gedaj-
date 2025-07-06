import feedparser

def fetch_cinema_news():
    feed = feedparser.parse("https://www.allocine.fr/rss/news_cinema.xml")
    if not feed.entries:
        return None
    first = feed.entries[0]
    return {
        "titre": first.title,
        "description": first.summary,
        "lien": first.link
    }