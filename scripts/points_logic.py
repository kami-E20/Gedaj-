import json
import os
from datetime import datetime

POINTS_FILE = "data/ranking.json"

def charger_points():
    """Charge les points des utilisateurs depuis le fichier JSON."""
    if not os.path.exists(POINTS_FILE):
        return {}
    with open(POINTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def sauvegarder_points_utilisateurs():
    """Sauvegarde les points actuels (fonction de sécurité) sans modification."""
    if not os.path.exists(POINTS_FILE):
        with open(POINTS_FILE, "w", encoding="utf-8") as f:
            json.dump({}, f, ensure_ascii=False, indent=2)
    else:
        with open(POINTS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        with open(POINTS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

def update_points(user_id, amount):
    """Met à jour les points d'un utilisateur donné."""
    user_id = str(user_id)
    data = charger_points()

    if user_id not in data:
        data[user_id] = {"points": 0, "last_active": "2025-01-01"}

    data[user_id]["points"] += amount
    data[user_id]["last_active"] = datetime.now().strftime("%Y-%m-%d")

    with open(POINTS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def get_points(user_id):
    """Retourne les points d’un utilisateur (ou 0 s’il n’existe pas encore)."""
    data = charger_points()
    user_id = str(user_id)
    return data.get(user_id, {}).get("points", 0)