import json
import os
from datetime import datetime

RANKING_FILE = "data/ranking.json"
REACTIONS_LOG = "data/reaction_logs.json"

# Réactions classées
REACTIONS_POSITIVES = ["❤️", "👍", "🔥", "👏", "💯", "🤩", "🥰", "😁", "😎", "😍"]
REACTIONS_NEGATIVES = ["👎", "😢", "😭", "😡", "🤬", "😠", "😒", "😞", "💔"]
REACTIONS_NEUTRES = ["😐", "🤔", "🙃", "😶"]
REACTIONS_DRÔLES = ["😂", "🤣", "😹", "😆", "😜", "😝"]
REACTIONS_SURPRISE = ["😮", "😲", "🤯", "😳"]
REACTIONS_INAPPROPRIÉES = ["💩", "🖕", "🖤", "🔞", "😤", "🤮", "🤢", "🧨", "🔫", "😈"]

# Toutes les réactions supportées
SUPPORTED_REACTIONS = (
    REACTIONS_POSITIVES +
    REACTIONS_NEGATIVES +
    REACTIONS_NEUTRES +
    REACTIONS_DRÔLES +
    REACTIONS_SURPRISE +
    REACTIONS_INAPPROPRIÉES
)

# Barème de points
REACTION_POINTS = {
    "positive": 2,
    "drôle": 2,
    "surprise": 1,
    "neutre": 0,
    "négative": -1,
    "inappropriée": -5
}

def get_reaction_type(emoji):
    if emoji in REACTIONS_POSITIVES:
        return "positive"
    if emoji in REACTIONS_NEGATIVES:
        return "négative"
    if emoji in REACTIONS_NEUTRES:
        return "neutre"
    if emoji in REACTIONS_DRÔLES:
        return "drôle"
    if emoji in REACTIONS_SURPRISE:
        return "surprise"
    if emoji in REACTIONS_INAPPROPRIÉES:
        return "inappropriée"
    return None

def handle_reaction(user_id, emoji):
    emoji_type = get_reaction_type(emoji)
    if not emoji_type:
        return  # Non pris en charge

    points = REACTION_POINTS.get(emoji_type, 0)
    user_id = str(user_id)

    # Charger ranking
    if os.path.exists(RANKING_FILE):
        with open(RANKING_FILE, "r", encoding="utf-8") as f:
            ranking = json.load(f)
    else:
        ranking = {}

    if user_id not in ranking:
        ranking[user_id] = {"points": 0, "last_active": "2025-01-01"}

    ranking[user_id]["points"] += points
    ranking[user_id]["last_active"] = datetime.now().strftime("%Y-%m-%d")

    with open(RANKING_FILE, "w", encoding="utf-8") as f:
        json.dump(ranking, f, indent=2, ensure_ascii=False)

    # Log de réaction
    if os.path.exists(REACTIONS_LOG):
        with open(REACTIONS_LOG, "r", encoding="utf-8") as f:
            logs = json.load(f)
    else:
        logs = {}

    logs.setdefault(user_id, []).append({
        "emoji": emoji,
        "type": emoji_type,
        "points": points,
        "date": datetime.now().isoformat()
    })

    with open(REACTIONS_LOG, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=2, ensure_ascii=False)