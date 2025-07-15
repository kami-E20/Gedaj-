import json
import os
from datetime import datetime

RANKING_FILE = "data/ranking.json"

def update_points(user_id, amount):
    os.makedirs("data", exist_ok=True)
    if os.path.exists(RANKING_FILE):
        with open(RANKING_FILE, "r", encoding="utf-8") as f:
            ranking = json.load(f)
    else:
        ranking = {}

    user_id = str(user_id)
    if user_id not in ranking:
        ranking[user_id] = {"points": 0, "last_active": "2025-01-01"}

    ranking[user_id]["points"] += amount
    ranking[user_id]["last_active"] = datetime.now().strftime("%Y-%m-%d")

    with open(RANKING_FILE, "w", encoding="utf-8") as f:
        json.dump(ranking, f, ensure_ascii=False, indent=2)

def register_inviter(bot):
    @bot.message_handler(commands=['inviter'])
    def handle_inviter(message):
        user_id = message.from_user.id
        update_points(user_id, 3)  # +3 points pour avoir invité (commande utilisée)

        texte = (
            "📢 *Invite tes amis à rejoindre Geekmania !*\n\n"
            "Plus on est nombreux, plus c'est fun 🎉\n"
            "Voici ton lien d'invitation unique :\n"
            "https://t.me/GEEKMANIA\n\n"
            "🔗 Chaque fois que tu utilises cette commande, tu gagnes *3 points* !\n"
            "Utilise aussi la commande /classement pour suivre ton évolution."
        )
        bot.send_message(message.chat.id, texte, parse_mode="Markdown")