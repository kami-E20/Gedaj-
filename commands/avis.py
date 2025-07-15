import json
import os

AVIS_FILE = "data/avis.json"
ADMINS = [5618445554, 879386491]  # Anthony & Kâmį

def register_avis(bot):
    @bot.message_handler(commands=['avis'])
    def handle_avis(message):
        parts = message.text.split(' ', 1)

        if len(parts) > 1 and parts[1].strip():
            # Cas 1 : L'avis est directement dans la commande
            save_avis(message, parts[1].strip())
        else:
            # Cas 2 : Demander l'avis séparément
            bot.send_message(
                message.chat.id,
                "✍️ *Quel est ton avis sur le film ou l’animation du jour ?*\n\n"
                "Donne-nous ton ressenti, ta note, ce que tu as aimé ou non.",
                parse_mode="Markdown"
            )
            bot.register_next_step_handler(message, lambda msg: save_avis(msg, msg.text.strip()))

    def save_avis(message, avis_text):
        user_id = message.from_user.id
        username = message.from_user.username or ""
        first_name = message.from_user.first_name or ""

        if not avis_text:
            bot.send_message(message.chat.id, "❌ Ton avis semble vide. Réessaie avec un vrai message.")
            return

        avis = {
            "user_id": user_id,
            "username": username,
            "first_name": first_name,
            "text": avis_text
        }

        os.makedirs("data", exist_ok=True)
        if os.path.exists(AVIS_FILE):
            with open(AVIS_FILE, "r", encoding="utf-8") as f:
                all_avis = json.load(f)
        else:
            all_avis = []

        all_avis.append(avis)

        with open(AVIS_FILE, "w", encoding="utf-8") as f:
            json.dump(all_avis, f, ensure_ascii=False, indent=2)

        bot.send_message(message.chat.id, "✅ Merci pour ton avis ! Il a bien été enregistré.")

        # 🔔 Envoi aux admins
        admin_message = (
            "📝 *Nouvel avis reçu !*\n\n"
            f"👤 *De :* `{first_name}` (@{username})\n"
            f"💬 *Avis :* `{avis_text}`"
        )
        for admin_id in ADMINS:
            bot.send_message(admin_id, admin_message, parse_mode="Markdown")