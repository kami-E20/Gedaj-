import json
from datetime import datetime

def fetch_anniversaires():
    today = datetime.now().strftime("%m-%d")
    anniversaires = []
    try:
        with open("data/celeb_anniversaires.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        for perso in data:
            if perso.get("date") == today:
                anniversaires.append(perso)
    except Exception as e:
        print("Erreur lecture anniversaires:", e)
    return anniversaires[:5]