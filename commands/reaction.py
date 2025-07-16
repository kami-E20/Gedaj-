from telebot import TeleBot
from telebot.types import Message
from datetime import datetime
import json
import os

# IDs des admins à notifier (Anthony et Kâmį)
ADMIN_IDS = [5618445554, 879386491]

# Seuil de réactions pour débloquer le lien
SEUIL_REACTIONS = 20

# Réactions valides à compter
REACTIONS_VALIDES = ["❤️", "👍"]

# Fichier de suivi des réactions (compteur simple)
REACTIONS_COUNT_FILE = "data/reactions_count.json"

# Fichier contenant message_id et chat_id du film publié
FILM_MESSAGE_FILE = "data/film_message.json"


def handle_reaction(bot: TeleBot, message: Message):
    """
    Gère une réaction reçue en réponse au message film du jour.
    Incrémente le compteur et envoie le lien aux admins si seuil atteint.
    """

    try:
        # On ne traite que les réactions valides en texte
        if not message.text or message.text not in REACTIONS_VALIDES:
            return

        # Vérifier que c’est une réaction en réponse au message du film
        if not message.reply_to_message:
            return

        # Charger le message film à suivre
        if not os.path.exists(FILM_MESSAGE_FILE):
            return  # Pas de film publié ou suivi

        with open(FILM_MESSAGE_FILE, "r", encoding="utf-8") as f:
            film_msg = json.load(f)

        if message.reply_to_message.message_id != film_msg["message_id"]:
            return  # Pas la bonne cible

        # Charger ou initialiser compteur des réactions
        if os.path.exists(REACTIONS_COUNT_FILE):
            with open(REACTIONS_COUNT_FILE, "r", encoding="utf-8") as f:
                reactions_data = json.load(f)
        else:
            reactions_data = {"count": 0}

        # Incrémenter le compteur
        reactions_data["count"] += 1

        # Sauvegarder le compteur mis à jour
        with open(REACTIONS_COUNT_FILE, "w", encoding="utf-8") as f:
            json.dump(reactions_data, f, ensure_ascii=False, indent=2)

        # Vérifier si seuil atteint
        if reactions_data["count"] == SEUIL_REACTIONS:
            envoyer_lien_aux_admins(bot)

    except Exception as e:
        print("❌ Erreur dans handle_reaction:", e)


def envoyer_lien_aux_admins(bot: TeleBot):
    """
    Envoie aux admins le lien de téléchargement et plateformes dès que le seuil est atteint.
    """

    try:
        jour = datetime.now().day
        film_file = f"data/films/{jour}.json"
        if not os.path.exists(film_file):
            print("❌ Fichier film du jour introuvable pour notification admins.")
            return

        with open(film_file, "r", encoding="utf-8") as f:
            film = json.load(f)

        message = (
            f"📥 Le film *{film.get('titre', 'Inconnu')}* a atteint {SEUIL_REACTIONS} réactions.\n\n"
            f"🎬 *Lien de téléchargement* : {film.get('lien_telechargement', 'Indisponible')}\n"
            f"📺 *Plateformes* : {', '.join(film.get('plateformes', []))}"
        )

        for admin_id in ADMIN_IDS:
            bot.send_message(admin_id, message, parse_mode="Markdown")

        print("✅ Notification de lien envoyée aux admins.")

    except Exception as e:
        print("❌ Erreur envoi lien aux admins:", e)