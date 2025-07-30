import json
import os
from scripts.points import ajouter_points

REACTION_LOGS = "data/reaction_logs.json"

def log_invitation(user_id):
    os.makedirs("data", exist_ok=True)
    user_id = str(user_id)

    if os.path.exists(REACTION_LOGS):
        with open(REACTION_LOGS, "r", encoding="utf-8") as f:
            logs = json.load(f)
    else:
        logs = {}

    if user_id not in logs:
        logs[user_id] = {"reactions": 0, "invitations": 0}

    logs[user_id]["invitations"] = logs[user_id].get("invitations", 0) + 1

    with open(REACTION_LOGS, "w", encoding="utf-8") as f:
        json.dump(logs, f, ensure_ascii=False, indent=2)

    return logs[user_id]["invitations"]

def register_inviter(bot):
    @bot.message_handler(commands=['inviter'])
    def handle_inviter(message):
        user_id = message.from_user.id
        ajouter_points(user_id, "invitation")
        total_invitations = log_invitation(user_id)

        texte = (
            "📢 *Invite tes amis à rejoindre Geekmania !*\n\n"
            "Plus on est nombreux, plus c'est fun 🎉\n"
            "Voici le lien d’invitation de Geekmania :\n"
            "➡️ https://t.me/GEEKMANIA\n\n"
            "🔗 Chaque fois que tu utilises cette commande, tu gagnes *10 points* !\n"
            f"📈 Tu as déjà utilisé cette commande *{total_invitations} fois*.\n"
            "Utilise aussi la commande /classement pour suivre ton évolution."
        )
        bot.send_message(message.chat.id, texte, parse_mode="Markdown")