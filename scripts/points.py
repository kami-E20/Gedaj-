import json
import os
from telebot import TeleBot

# Chargement du token pour test (via variable d'env)
TOKEN = os.getenv("BOT_TOKEN", "INACTIF")
bot = TeleBot(TOKEN) if ":" in TOKEN else None

POINTS_BARÈME = {
    "reaction": 1,
    "quiz_participation": 3,
    "quiz_correct": 5,
    "commentaire": 2,
    "invitation": 10
}

RANKING_PATH = "data/ranking.json"

def ajouter_points(user_id, action):
    try:
        with open(RANKING_PATH, "r", encoding="utf-8") as f:
            scores = json.load(f)
    except FileNotFoundError:
        scores = {}

    user_id = str(user_id)
    points = POINTS_BARÈME.get(action, 0)
    scores[user_id] = scores.get(user_id, 0) + points

    with open(RANKING_PATH, "w", encoding="utf-8") as f:
        json.dump(scores, f, indent=4)
    print(f"✅ {points} points ajoutés à {user_id} pour action '{action}'.")

def publier_meilleurs_abonnes(chat_id=None):
    try:
        with open(RANKING_PATH, "r", encoding="utf-8") as f:
            scores = json.load(f)
        top = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:5]

        message = "🏅 *Top 5 abonnés de la semaine* :\n\n"
        for i, (uid, pts) in enumerate(top, 1):
            message += f"{i}. ID `{uid}` — *{pts} pts*\n"

        if chat_id and bot:
            bot.send_message(chat_id, message, parse_mode="Markdown")
        else:
            print(message)
    except Exception as e:
        print(f"❌ Erreur publication top abonnés : {e}")

def publier_abonnes_du_mois(chat_id=None):
    try:
        with open(RANKING_PATH, "r", encoding="utf-8") as f:
            scores = json.load(f)
        top = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:3]

        message = "🎁 *Récompenses du mois* :\n\n"
        for i, (uid, pts) in enumerate(top, 1):
            reward = "🏆" if i == 1 else "🥈" if i == 2 else "🥉"
            message += f"{reward} {i}. ID `{uid}` — *{pts} pts*\n"

        if chat_id and bot:
            bot.send_message(chat_id, message, parse_mode="Markdown")
        else:
            print(message)
    except Exception as e:
        print(f"❌ Erreur publication mensuelle : {e}")


# TEST MANUEL
if __name__ == "__main__":
    publier_meilleurs_abonnes()
    publier_abonnes_du_mois()