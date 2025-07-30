import json
import os
from datetime import datetime

SUGGESTION_FILE = "data/suggestions.json"
ADMINS = [5618445554, 879386491]  # Anthony & Kâmį

def register_suggestion(bot):
    @bot.message_handler(commands=['suggestion'])
    def ask_for_suggestion(message):
        bot.send_message(
            message.chat.id,
            "💡 *Quelle est ta suggestion ?*\n\n"
            "Envoie-moi maintenant le titre d’un film, une série, un manga ou une animation que tu aimerais voir apparaître sur Geekmania.",
            parse_mode="Markdown"
        )
        bot.register_next_step_handler(message, save_suggestion)

    def save_suggestion(message):
        user_id = message.from_user.id
        username = message.from_user.username
        first_name = message.from_user.first_name or "Utilisateur"
        suggestion_text = message.text.strip()

        if not suggestion_text:
            bot.send_message(message.chat.id, "❌ Suggestion vide. Réessaie avec un vrai titre.")
            return

        # Construction de l'entrée
        suggestion = {
            "user_id": user_id,
            "username": username,
            "first_name": first_name,
            "text": suggestion_text,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M")
        }

        os.makedirs("data", exist_ok=True)

        try:
            with open(SUGGESTION_FILE, "r", encoding="utf-8") as f:
                suggestions = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            suggestions = []

        suggestions.append(suggestion)

        with open(SUGGESTION_FILE, "w", encoding="utf-8") as f:
            json.dump(suggestions, f, ensure_ascii=False, indent=2)

        bot.send_message(message.chat.id, "✅ Merci ! Ta suggestion a bien été enregistrée.")

        # 🔔 Notification aux admins
        mention = f"(@{username})" if username else ""
        admin_message = (
            "📬 *Nouvelle suggestion reçue !*\n\n"
            f"👤 *De :* `{first_name}` {mention}\n"
            f"🕒 *Date :* {suggestion['date']}\n"
            f"🎥 *Suggestion :* `{suggestion_text}`"
        )
        for admin_id in ADMINS:
            bot.send_message(admin_id, admin_message, parse_mode="Markdown")