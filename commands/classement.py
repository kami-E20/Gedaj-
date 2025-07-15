import json
import os

RANKING_FILE = "data/ranking.json"
USERS_FILE = "data/users.json"  # Contient infos utilisateur (id, username, first_name)

def register_classement(bot):
    @bot.message_handler(commands=['classement'])
    def handle_classement(message):
        if not os.path.exists(RANKING_FILE) or not os.path.exists(USERS_FILE):
            bot.send_message(message.chat.id, "⚠️ Aucun classement disponible pour le moment.")
            return

        with open(RANKING_FILE, "r", encoding="utf-8") as f:
            ranking = json.load(f)

        with open(USERS_FILE, "r", encoding="utf-8") as f:
            users = json.load(f)

        if not ranking:
            bot.send_message(message.chat.id, "⚠️ Aucun classement disponible pour le moment.")
            return

        # Trier les utilisateurs par points décroissants
        sorted_ranking = sorted(ranking.items(), key=lambda x: x[1].get("points", 0), reverse=True)
        top_10 = sorted_ranking[:10]

        classement_text = "🏆 *Top 10 des Fans Geekmania*\n\n"

        for i, (user_id, data) in enumerate(top_10, start=1):
            points = data.get("points", 0)
            user_info = users.get(user_id, {})
            username = user_info.get("username")
            first_name = user_info.get("first_name", "Utilisateur")
            display_name = f"@{username}" if username else first_name
            classement_text += f"{i}. {display_name} — {points} points\n"

        bot.send_message(message.chat.id, classement_text, parse_mode="Markdown")