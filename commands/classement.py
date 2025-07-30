import json
import os

RANKING_FILE = "data/ranking.json"
USERS_FILE = "data/users.json"

def register_classement(bot):
    @bot.message_handler(commands=['classement'])
    def handle_classement(message):
        if not os.path.exists(RANKING_FILE) or not os.path.exists(USERS_FILE):
            bot.send_message(message.chat.id, "⚠️ Aucun classement disponible pour l’instant.")
            return

        with open(RANKING_FILE, "r", encoding="utf-8") as f:
            ranking = json.load(f)

        with open(USERS_FILE, "r", encoding="utf-8") as f:
            users = json.load(f)

        if not ranking:
            bot.send_message(message.chat.id, "⚠️ Aucun fan actif trouvé pour le moment.")
            return

        # 🔢 Top 10 par points
        sorted_ranking = sorted(
            ranking.items(),
            key=lambda x: x[1].get("points", 0),
            reverse=True
        )[:10]

        if not sorted_ranking:
            bot.send_message(message.chat.id, "📭 Aucun utilisateur n’a encore gagné de points.")
            return

        classement_text = "🏆 *Top 10 des Fans Geekmania*\n\n"
        medailles = ["🥇", "🥈", "🥉"]

        for i, (user_id, data) in enumerate(sorted_ranking, start=1):
            user_id = str(user_id)
            points = data.get("points", 0)
            user_info = users.get(user_id, {})
            username = user_info.get("username")
            first_name = user_info.get("first_name", "Utilisateur")

            # 🎭 Nom affiché
            if username:
                display_name = f"{first_name} (@{username})"
            else:
                display_name = f"{first_name}"

            emoji = medailles[i - 1] if i <= 3 else f"{i}."

            classement_text += f"{emoji} {display_name} — *{points} pts*\n"

        bot.send_message(message.chat.id, classement_text, parse_mode="Markdown")