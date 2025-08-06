import json, os
from datetime import datetime
from telebot.types import Message

AVIS_FILE = "data/avis.json"
ADMINS = [5618445554, 879386491]

def register_avis(bot):
    @bot.message_handler(commands=['avis'])
    def handle_avis_command(message: Message):
        text = message.text.replace("/avis", "").strip()
        if text:
            save_avis(bot, message, text)
        else:
            bot.send_message(
                message.chat.id,
                "🗣️ *Laisse ton avis !*\n\n👉 Tu peux répondre à ce message OU écrire `/avis ton avis ici`",
                parse_mode="Markdown"
            )
            bot.register_next_step_handler(message, ask_avis)

    def ask_avis(message: Message):
        save_avis(bot, message, message.text.strip())

def save_avis(bot, message, text):
    if not text:
        bot.send_message(message.chat.id, "❌ Avis vide. Réessaie.")
        return

    avis = {
        "user_id": message.from_user.id,
        "username": message.from_user.username or "",
        "first_name": message.from_user.first_name or "",
        "text": text,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

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

    msg = (
        "🗣️ *Nouvel avis !*\n"
        f"👤 {avis['first_name']} (@{avis['username']})\n"
        f"📅 {avis['date']}\n"
        f"💬 {avis['text']}"
    )
    for admin_id in ADMINS:
        bot.send_message(admin_id, msg, parse_mode="Markdown")