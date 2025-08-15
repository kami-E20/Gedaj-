import requests
import feedparser
from datetime import datetime
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
import logging
import html

# ========== CONFIG ==========
ADMIN_IDS = [5618445554, 879386491]  # Anthony & Kâmį
CHANNEL_ID = "@GEEKMANIA"
RSS_FILM_SERIE = [
    "https://www.allocine.fr/rss/news.xml",
    "https://www.premiere.fr/rss/actu"
]
RSS_ANIME = [
    "https://www.animenewsnetwork.com/all/rss.xml?ann-edition=us"
]
ANILIST_API = "https://graphql.anilist.co"

# ========== LOGGING ==========
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ========== GET FILM/SERIE NEWS ==========
def get_film_serie_news():
    news_list = []
    for feed_url in RSS_FILM_SERIE:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries[:3]:
            title = entry.title
            link = entry.link
            summary = html.unescape(entry.summary) if hasattr(entry, "summary") else ""
            image_url = ""
            if "media_content" in entry and entry.media_content:
                image_url = entry.media_content[0]["url"]
            news_list.append({
                "title": title,
                "link": link,
                "summary": summary,
                "image": image_url
            })
    return news_list

# ========== GET ANIME NEWS ==========
def get_anime_news():
    news_list = []
    for feed_url in RSS_ANIME:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries[:3]:
            title = entry.title
            link = entry.link
            summary = html.unescape(entry.summary) if hasattr(entry, "summary") else ""
            image_url = ""
            if "media_content" in entry and entry.media_content:
                image_url = entry.media_content[0]["url"]
            news_list.append({
                "title": title,
                "link": link,
                "summary": summary,
                "image": image_url
            })
    return news_list

# ========== GET UPCOMING FROM ANILIST ==========
def get_anilist_upcoming():
    query = """
    query {
      Page(perPage: 5) {
        media(type: ANIME, sort: START_DATE, status: NOT_YET_RELEASED) {
          title {
            romaji
            english
          }
          startDate {
            year
            month
            day
          }
          siteUrl
          coverImage {
            extraLarge
          }
        }
      }
    }
    """
    try:
        response = requests.post(ANILIST_API, json={"query": query})
        data = response.json()
        upcoming = []
        for anime in data["data"]["Page"]["media"]:
            title = anime["title"]["english"] or anime["title"]["romaji"]
            date = f"{anime['startDate']['day']}/{anime['startDate']['month']}/{anime['startDate']['year']}"
            url = anime["siteUrl"]
            img = anime["coverImage"]["extraLarge"]
            upcoming.append({
                "title": title,
                "release_date": date,
                "link": url,
                "image": img
            })
        return upcoming
    except Exception as e:
        logger.error(f"Erreur AniList: {e}")
        return []

# ========== FORMAT NEWS MESSAGE ==========
def format_news_message():
    films = get_film_serie_news()
    animes = get_anime_news()
    upcoming = get_anilist_upcoming()

    message = "🎬 **ACTUALITÉS FILMS & SÉRIES**\n\n"
    for item in films:
        message += f"🔹 [{item['title']}]({item['link']})\n"
        if item['summary']:
            message += f"_{item['summary']}_\n"
        if item['image']:
            message += f"[Affiche]({item['image']})\n"
        message += "\n"

    message += "\n🍥 **ACTUALITÉS ANIMÉS**\n\n"
    for item in animes:
        message += f"🔹 [{item['title']}]({item['link']})\n"
        if item['summary']:
            message += f"_{item['summary']}_\n"
        if item['image']:
            message += f"[Visuel]({item['image']})\n"
        message += "\n"

    message += "\n📅 **SORTIES PROCHAINES (AniList)**\n\n"
    for item in upcoming:
        message += f"🔹 **{item['title']}** — 📆 {item['release_date']}\n"
        message += f"[Plus d'infos]({item['link']}) | [Image]({item['image']})\n\n"

    message += "\n— _Geekmania_"
    return message

# ========== PUBLISH NEWS ==========
def publish_news(context: CallbackContext):
    msg = format_news_message()
    context.bot.send_message(chat_id=CHANNEL_ID, text=msg, parse_mode="Markdown", disable_web_page_preview=False)
    logger.info("News publiées automatiquement.")

# ========== FORCE NEWS (ADMIN) ==========
def force_news(update: Update, context: CallbackContext):
    if update.effective_user.id not in ADMIN_IDS:
        update.message.reply_text("❌ Vous n'êtes pas autorisé à forcer la publication.")
        return
    msg = format_news_message()
    context.bot.send_message(chat_id=CHANNEL_ID, text=msg, parse_mode="Markdown", disable_web_page_preview=False)
    update.message.reply_text("✅ News publiées manuellement.")
    logger.info(f"News forcées par {update.effective_user.username}")

# ========== INIT HANDLER ==========
def init_forcenews_handlers(dispatcher):
    dispatcher.add_handler(CommandHandler("forcenews", force_news))

# ========== SCHEDULER SETUP ==========
def schedule_news(job_queue):
    job_queue.run_daily(publish_news, time=datetime.time(hour=9, minute=0))  # 09h00 Kinshasa