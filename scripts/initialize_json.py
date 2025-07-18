# scripts/initialize_json.py

import os
import json

DATA_DIR = "data"
BACKUP_DIR = "backup"

REQUIRED_FILES = {
    f"{DATA_DIR}/users.json": {},
    f"{DATA_DIR}/suggestions.json": [],
    f"{DATA_DIR}/avis.json": [],
    f"{DATA_DIR}/fanpass.json": {},
    f"{DATA_DIR}/ranking.json": {},
    f"{DATA_DIR}/reaction_logs.json": {},
    f"{DATA_DIR}/lockdown.json": {"active": False},
    f"{DATA_DIR}/defis.json": {
        "2025": {
            "juillet": {
                "semaine_1": {"titre": "", "description": "", "points": 0},
                "semaine_2": {"titre": "", "description": "", "points": 0},
                "semaine_3": {"titre": "", "description": "", "points": 0},
                "semaine_4": {"titre": "", "description": "", "points": 0}
            }
        }
    },
    f"{DATA_DIR}/celeb_anniversaires.json": [],
    f"{DATA_DIR}/text_intelligence.json": {},

    f"{BACKUP_DIR}/users_backup.json": {},
    f"{BACKUP_DIR}/ranking_backup.json": {},
    f"{BACKUP_DIR}/reaction_logs_backup.json": {},
}

# Crée les quiz_01.json à quiz_31.json
for i in range(1, 32):
    path = f"{DATA_DIR}/quiz/quiz_{i}.json"
    REQUIRED_FILES[path] = {
        "question": "",
        "options": [],
        "reponse": "",
        "explication": ""
    }

# Crée les films 01.json à 31.json
for i in range(1, 32):
    path = f"{DATA_DIR}/films/{i:02}.json"
    REQUIRED_FILES[path] = {
        "titre": "",
        "description": "",
        "image": "",
        "plateformes": [],
        "annee": "",
        "pays": "",
        "genre": [],
        "lien_telechargement": ""
    }

def create_missing_files():
    for path, default_content in REQUIRED_FILES.items():
        folder = os.path.dirname(path)
        os.makedirs(folder, exist_ok=True)

        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8") as f:
                json.dump(default_content, f, indent=4)
            print(f"✅ Fichier JSON créé : {path}")
        else:
            print(f"🟡 Déjà existant : {path}")

if __name__ == "__main__":
    create_missing_files()
