import datetime
import json
import os

# Fichier de données locales avec les anniversaires connus
ACTEURS_FILE = os.path.join("data", "anniversaires.json")

def load_anniversaire_data():
    if not os.path.exists(ACTEURS_FILE):
        return []
    with open(ACTEURS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def fetch_anniversaires():
    aujourd_hui = datetime.datetime.now().strftime("%m-%d")
    tous_les_acteurs = load_anniversaire_data()
    return [
        {
            "nom": acteur["nom"],
            "role": acteur.get("role", "Artiste"),
            "anecdote": acteur.get("anecdote", "Pas d’anecdote disponible."),
            "date": acteur["date"],
            "film_recommande": acteur.get("film", "Non spécifié.")
        }
        for acteur in tous_les_acteurs if acteur["date"] == aujourd_hui
    ]