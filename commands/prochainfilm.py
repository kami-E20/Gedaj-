import json
import os

FILMS_A_VENIR_FILE = "data/prochains_films.json"

def get_prochains_films():
    if not os.path.exists(FILMS_A_VENIR_FILE):
        return []
    with open(FILMS_A_VENIR_FILE, "r", encoding="utf-8") as f:
        return json.load(f)  # On attend une liste de dicts avec titre, date, description

def register_prochainfilm(bot):
    @bot.message_handler(commands=['prochainfilm'])
    def handle_prochainfilm(message):
        films = get_prochains_films()
        if not films:
            bot.send_message(message.chat.id, "🎬 Aucun film à venir pour le moment.")
            return

        texte = "🎬 *Prochaines sorties cinéma :*\n\n"
        for film in films[:5]:  # On limite à 5 films pour ne pas spammer
            titre = film.get("titre", "Titre inconnu")
            date_sortie = film.get("date_sortie", "Date inconnue")
            description = film.get("description", "")
            texte += f"• *{titre}* — Sortie le {date_sortie}\n{description}\n\n"

        bot.send_message(message.chat.id, texte, parse_mode="Markdown")