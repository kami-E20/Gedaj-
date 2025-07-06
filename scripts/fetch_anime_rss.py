import feedparser

def fetch_anime_rss():
    feed = feedparser.parse("https://www.animenewsnetwork.com/all/rss.xml")
    if not feed.entries:
        return None
    first = feed.entries[0]
    return {
        "titre": first.title,
        "description": first.summary,
        "lien": first.link
    }