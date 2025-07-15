import os
import json
from datetime import datetime

# 📁 Chemins des fichiers JSON
RANKING_FILE = "data/ranking.json"
FANPASS_FILE = "data/fanpass.json"

# 🏆 Barème des niveaux Fan Pass
LEVELS = [
    (0, "🎬 Débutant(e)"),
    (50, "🎯 Explorateur"),
    (120, "🍿 Fan Actif"),
    (250, "📽️ Cinéphile"),
    (500, "🧠 Geek confirmé"),
    (1000, "🌟 Légende Geekmania")
]

# 📥 Lecture JSON
def load_json(path):
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

# 💾 Sauvegarde JSON
def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

# 🎯 Obtenir le niveau selon les points
def get_level(points):
    for seuil, titre in reversed(LEVELS):
        if points >= seuil:
            return titre
    return LEVELS[0][1]

# ➕ Ajouter des points
def add_points(user_id, nom, points, raison=""):
    user_id = str(user_id)

    ranking = load_json(RANKING_FILE)
    fanpass = load_json(FANPASS_FILE)

    # ✅ MAJ classement
    if user_id not in ranking:
        ranking[user_id] = {"nom": nom, "score": 0, "logs": []}
    ranking[user_id]["score"] += points
    ranking[user_id]["logs"].append({
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "points": points,
        "raison": raison
    })

    # 🎟️ MAJ Fan Pass
    if user_id not in fanpass:
        fanpass[user_id] = {"nom": nom, "points": 0, "niveau": "🎬 Débutant(e)"}
    fanpass[user_id]["points"] += points
    fanpass[user_id]["niveau"] = get_level(fanpass[user_id]["points"])

    # 💾 Sauvegarde
    save_json(RANKING_FILE, ranking)
    save_json(FANPASS_FILE, fanpass)

# 📊 Score global d’un utilisateur
def get_user_score(user_id):
    user_id = str(user_id)
    ranking = load_json(RANKING_FILE)
    return ranking.get(user_id, {}).get("score", 0)

# 🎟️ Récupérer les infos Fan Pass
def get_user_fanpass(user_id):
    user_id = str(user_id)
    fanpass = load_json(FANPASS_FILE)
    return fanpass.get(user_id, {
        "points": 0,
        "niveau": "🎬 Débutant(e)"
    })

# 🥇 Top utilisateurs (classement)
def get_top_users(n=5):
    ranking = load_json(RANKING_FILE)
    sorted_users = sorted(ranking.items(), key=lambda x: x[1]["score"], reverse=True)
    return sorted_users[:n]

# 📖 Historique des points d’un utilisateur
def get_user_logs(user_id):
    user_id = str(user_id)
    ranking = load_json(RANKING_FILE)
    return ranking.get(user_id, {}).get("logs", [])