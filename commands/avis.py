import json
import os
from datetime import datetime

AVIS_FILE = "data/avis.json"
ADMINS = [5618445554, 879386491]

def register_avis(bot):
    @bot.message_handler(commands=['avis'])
    def ask_for_avis(message):
        bot.send_message(
            message.chat.id,
            "🗣️ *Laisse ton avis sur un film, série ou animation !*\n\nÉcris ton message ci-dessous 👇",
            parse_mode="Markdown"
        )
        bot.register_next_step_handler(message, save_avis)

    def save_avis(message):
        avis = {
            "user_id": message.from_user.id,
            "username": message.from_user.username or "",
            "first_name": message.from_user.first_name or "",
            "text": message.text.strip(),
            "date": datetime.now().strftime("%Y-%m-%d %H:%M")
        }

        if not avis["text"]:
            bot.send_message(message.chat.id, "❌ Avis vide. Réessaie.")
            return

        os.makedirs("data", exist_ok=True)
        try:
            with open(AVIS_FILE, "r", encoding="utf-8") as f:
                all_avis = json.load(f)
        except FileNotFoundError:
            all_avis = []

        all_avis.append(avis)
        with open(AVIS_FILE, "w", encoding="utf-8") as f:
            json.dump(all_avis, f, ensure_ascii=False, indent=2)

        bot.send_message(message.chat.id, "✅ Merci pour ton avis ! Il a été enregistré.")

        # 🔔 Notification admins
        msg = (
            "🗣️ *Nouvel avis utilisateur !*\n"
            f"👤 De : `{avis['first_name']}` (@{avis['username']})\n"
            f"📅 Date : {avis['date']}\n"
            f"💬 Avis : {avis['text']}"
        )
        for admin_id in ADMINS:
            bot.send_message(admin_id, msg, parse_mode="Markdown")