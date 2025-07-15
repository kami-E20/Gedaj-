# initialize_json.py

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
    f"{BACKUP_DIR}/users_backup.json": {},
    f"{BACKUP_DIR}/ranking_backup.json": {},
    f"{BACKUP_DIR}/reaction_logs_backup.json": {},
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

def create_quiz_files():
    quiz_dir = os.path.join(DATA_DIR, "quiz")
    os.makedirs(quiz_dir, exist_ok=True)

    model = {
        "question": "",
        "options": ["", "", "", ""],
        "correct_index": 0
    }

    for i in range(1, 32):
        filename = f"quiz_{i:02d}.json"
        path = os.path.join(quiz_dir, filename)
        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8") as f:
                json.dump(model, f, indent=4)
            print(f"✅ Quiz créé : {path}")
        else:
            print(f"🟡 Quiz existant : {path}")

def create_film_files():
    films_dir = os.path.join(DATA_DIR, "films")
    os.makedirs(films_dir, exist_ok=True)

    model = {
        "titre": "",
        "description": "",
        "image_url": "",
        "categorie": "",
        "annee": "",
        "pays": "",
        "realisateur": "",
        "plateformes": []
    }

    for i in range(1, 32):
        filename = f"{i:02d}.json"
        path = os.path.join(films_dir, filename)
        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8") as f:
                json.dump(model, f, indent=4)
            print(f"✅ Film créé : {path}")
        else:
            print(f"🟡 Film existant : {path}")

if __name__ == "__main__":
    create_missing_files()
    create_quiz_files()
    create_film_files()
    print("\n📦 Initialisation JSON terminée.")