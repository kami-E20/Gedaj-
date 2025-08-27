import datetime
from telebot import TeleBot

ADMINS_ID = [5618445554, 879386491]

# ---- Imports internes ----
from commands_admin.anniversaire import (
    get_today_anniversaires,
    format_anniversaire_message
)
from scripts.fetch_cinema_news import fetch_cinema_news
from scripts.fetch_anilist_news import fetch_anilist_news
from scripts.notify_sorties import notify_admins_sorties


def notifier_admins_daily(bot: TeleBot):
    """
    Envoie une notification quotidienne aux admins :
    - Anniversaires d’acteurs/réalisateurs/scénaristes
    - Actus cinéma
    - Actus anime/manga
    - Sorties à venir
    """

    today = datetime.datetime.now().strftime("%d/%m/%Y")

    # ---- Anniversaires ----
    anniversaires_text = f"🎂 *Anniversaires du {today} :*\n"
    try:
        anniversaires = get_today_anniversaires()
        if anniversaires:
            anniversaires_text += "\n".join(
                [format_anniversaire_message(a) for a in anniversaires]
            )
        else:
            anniversaires_text += "Aucun anniversaire trouvé aujourd'hui."
    except Exception:
        anniversaires_text += "Erreur lors de la récupération."

    # ---- Actus cinéma ----
    cinema_text = "🎬 *Actualités cinéma :*\n"
    try:
        news_cinema = fetch_cinema_news()
        if news_cinema:
            cinema_text += "\n".join(news_cinema)
        else:
            cinema_text += "Pas d’actualité disponible."
    except Exception:
        cinema_text += "Erreur lors de la récupération."

    # ---- Actus anime/manga ----
    anime_text = "📺 *Actualités anime/manga :*\n"
    try:
        news_anime = fetch_anilist_news()
        if news_anime:
            anime_text += "\n".join(news_anime)
        else:
            anime_text += "Pas d’actualité disponible."
    except Exception:
        anime_text += "Erreur lors de la récupération."

    # ---- Sorties à venir ----
    sorties_text = "📅 *Sorties à venir :*\n"
    try:
        notify_admins_sorties(bot)  # envoi direct, pas de preview
        sorties_text += "✅ Sorties envoyées séparément aux admins."
    except Exception:
        sorties_text += "⚠️ Aucune donnée disponible."

    # ---- Fusion finale ----
    message = (
        f"{anniversaires_text}\n\n"
        f"{cinema_text}\n\n"
        f"{anime_text}\n\n"
        f"{sorties_text}"
    )

    # ---- Envoi aux admins ----
    for admin_id in ADMINS_ID:
        try:
            bot.send_message(admin_id, message, parse_mode="Markdown")
        except Exception as e:
            print(f"Erreur envoi admin {admin_id}: {e}")