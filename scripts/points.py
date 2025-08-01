import json
from datetime import datetime
import os

POINTS_FILE = "data/ranking.json"
LOG_FILE = "data/reaction_logs.json"

POINTS_BARÈME = {
    "reaction": 1,
    "reaction_neg": 1,
    "reaction_toxique": -5,
    "quiz_participation": 3,
    "quiz_correct": 5,
    "commentaire": 2,
    "invitation": 10
}

def ajouter_points(user_id, action):
    points = POINTS_BARÈME.get(action, 0)
    user_id = str(user_id)

    if not os.path.exists(POINTS_FILE):
        data = {}
    else:
        with open(POINTS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

    if user_id not in data:
        data[user_id] = {"points": 0, "last_active": "2025-01-01"}

    data[user_id]["points"] += points
    data[user_id]["last_active"] = datetime.now().strftime("%Y-%m-%d")

    with open(POINTS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def publier_meilleurs_abonnes():
    try:
        with open(POINTS_FILE, "r", encoding="utf-8") as f:
            scores = json.load(f)
        top = sorted(scores.items(), key=lambda x: x[1].get("points", 0), reverse=True)[:5]
        print("🏅 Top abonnés de la semaine :")
        for i, (uid, pts) in enumerate(top, 1):
            print(f"{i}. ID {uid} — {pts['points']} pts")
    except:
        print("❌ Erreur publication top abonnés.")