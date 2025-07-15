import json
import os

SUGGESTION_FILE = "data/suggestions.json"

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
        suggestion_text = message.text.strip()

        if not suggestion_text:
            bot.send_message(message.chat.id, "❌ Suggestion vide. Réessaie avec un vrai titre.")
            return

        suggestion = {
            "user_id": user_id,
            "username": message.from_user.username or "",
            "text": suggestion_text
        }

        os.makedirs("data", exist_ok=True)
        if os.path.exists(SUGGESTION_FILE):
            with open(SUGGESTION_FILE, "r", encoding="utf-8") as f:
                suggestions = json.load(f)
        else:
            suggestions = []

        suggestions.append(suggestion)

        with open(SUGGESTION_FILE, "w", encoding="utf-8") as f:
            json.dump(suggestions, f, ensure_ascii=False, indent=2)

        bot.send_message(message.chat.id, "✅ Merci ! Ta suggestion a bien été enregistrée.")