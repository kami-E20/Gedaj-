import json

POINTS_BARÈME = {
    "reaction": 1,
    "quiz_participation": 3,
    "quiz_correct": 5,
    "commentaire": 2,
    "invitation": 10
}

def ajouter_points(user_id, action):
    try:
        with open("data/ranking.json", "r") as f:
            scores = json.load(f)
    except FileNotFoundError:
        scores = {}

    user_id = str(user_id)
    points = POINTS_BARÈME.get(action, 0)
    scores[user_id] = scores.get(user_id, 0) + points

    with open("data/ranking.json", "w") as f:
        json.dump(scores, f, indent=2)


def publier_meilleurs_abonnes():
    try:
        with open("data/ranking.json", "r") as f:
            scores = json.load(f)
        top = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:5]
        print("🏅 Top abonnés de la semaine :")
        for i, (uid, pts) in enumerate(top, 1):
            print(f"{i}. ID {uid} — {pts} pts")
    except:
        print("Erreur publication top abonnés.")

def publier_abonnes_du_mois():
    print("🎁 Publication des récompenses mensuelles...")