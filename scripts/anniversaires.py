import datetime
import json
import os

# Nom correct du fichier JSON contenant les anniversaires
ANNIV_FILE = os.path.join("data", "celeb_anniversaires.json")

def load_anniversaire_data():
    if not os.path.exists(ANNIV_FILE):
        return []
    with open(ANNIV_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def fetch_anniversaires():
    """Retourne la liste des célébrités dont c'est l'anniversaire aujourd'hui."""
    aujourd_hui = datetime.datetime.now().strftime("%m-%d")
    tous = load_anniversaire_data()
    return [
        {
            "nom": celeb["nom"],
            "role": celeb.get("role", "Artiste"),
            "anecdote": celeb.get("anecdote", "Aucune anecdote disponible."),
            "date": celeb["date"],
            "film_recommande": celeb.get("film", "Film non précisé")
        }
        for celeb in tous if celeb["date"] == aujourd_hui
    ]