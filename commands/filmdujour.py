# commands/filmdujour.py
import json
import os
from datetime import datetime
from telebot.types import Message
from telebot import TeleBot

FILMS_FILE = "data/film/film.json"
AUTHORIZED_ADMINS = [5618445554, 879386491]  # Anthony & Kâmį

def _load_films():
    try:
        with open(FILMS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, list):
                raise ValueError("Le JSON des films doit être une liste d'objets.")
            return data
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"[filmdujour] Erreur de lecture JSON: {e}")
        return []

def _pick_today_film(films):
    """Choisit le film du jour par index (jour du mois - 1)."""
    if not films:
        return None, None
    idx = datetime.now().day - 1  # 0..30 pour 31 films
    if idx >= len(films):
        idx = idx % len(films)
    return films[idx], idx

def _find_film_by_index(films, idx_str):
    """Permet /forcefilm 12 -> index 11 (humain 1-based)."""
    try:
        i = int(idx_str)
        if i <= 0:
            return None, None
        py_idx = i - 1
        if 0 <= py_idx < len(films):
            return films[py_idx], py_idx
    except Exception:
        pass
    return None, None

def _find_film_by_title(films, query):
    q = query.strip().lower()
    for i, f in enumerate(films):
        if q in f.get("titre", "").lower():
            return f, i
    return None, None

def _format_film_msg(film, idx=None):
    titre = film.get("titre", "Titre inconnu")
    annee = film.get("annee") or film.get("année") or "—"
    genre = film.get("genre", "—")
    synopsis = film.get("synopsis", "—")
    affiche = film.get("affiche", "")

    header = f"🎬 *Film du jour*"
    if idx is not None:
        header += f" — #{idx+1}"

    msg = (
        f"{header}\n\n"
        f"• *Titre* : {titre}\n"
        f"• *Année* : {annee}\n"
        f"• *Genre* : {genre}\n\n"
        f"📝 *Synopsis* :\n{synopsis}\n\n"
    )
    if affiche:
        msg += f"🖼 *Affiche* : {affiche}\n\n"

    msg += "❤️ Réagis à ce message pour soutenir la sélection du jour."
    return msg

def _send_film(bot: TeleBot, chat_id: int, film: dict, idx: int | None):
    text = _format_film_msg(film, idx)
    bot.send_message(chat_id, text, parse_mode="Markdown")

def register_filmdujour(bot: TeleBot):
    @bot.message_handler(commands=['filmdujour'])
    def filmdujour_cmd(message: Message):
        films = _load_films()
        if not films:
            bot.reply_to(message, "⚠️ Aucun film trouvé. Ajoute des entrées dans `data/films/films.json`.")
            return

        film, idx = _pick_today_film(films)
        if not film:
            bot.reply_to(message, "⚠️ Impossible de sélectionner le film du jour.")
            return

        _send_film(bot, message.chat.id, film, idx)

    @bot.message_handler(commands=['forcefilm'])
    def forcefilm_cmd(message: Message):
        # 🔒 Admin only
        if message.from_user.id not in AUTHORIZED_ADMINS:
            bot.reply_to(message, "⛔ Cette commande est réservée aux administrateurs.")
            return

        films = _load_films()
        if not films:
            bot.reply_to(message, "⚠️ Aucun film trouvé dans `data/films/films.json`.")
            return

        # Parse arguments après la commande
        parts = message.text.split(maxsplit=1)
        chosen = None
        idx = None

        if len(parts) == 1:
            # Pas d’argument -> forcer le film du jour
            chosen, idx = _pick_today_film(films)
        else:
            arg = parts[1].strip()
            # Essayer index 1-based
            chosen, idx = _find_film_by_index(films, arg)
            if chosen is None:
                # Essayer titre partiel
                chosen, idx = _find_film_by_title(films, arg)

        if chosen is None:
            bot.reply_to(
                message,
                "❌ Film introuvable. Utilise :\n"
                "• `/forcefilm` (sans argument) pour envoyer le film du jour\n"
                "• `/forcefilm 12` pour envoyer le #12\n"
                "• `/forcefilm Inception` pour chercher par titre",
                parse_mode="Markdown"
            )
            return

        _send_film(bot, message.chat.id, chosen, idx)
        bot.send_message(message.chat.id, "✅ Film publié manuellement (admin).")