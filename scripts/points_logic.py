import json
import os
from datetime import datetime

POINTS_FILE = "data/ranking.json"

def update_points(user_id, amount):
    user_id = str(user_id)
    if not os.path.exists(POINTS_FILE):
        data = {}
    else:
        with open(POINTS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

    if user_id not in data:
        data[user_id] = {"points": 0, "last_active": "2025-01-01"}

    data[user_id]["points"] += amount
    data[user_id]["last_active"] = datetime.now().strftime("%Y-%m-%d")

    with open(POINTS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)