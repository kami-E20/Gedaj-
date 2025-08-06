import json, os
from datetime import datetime
from telebot.types import Message

SUG_FILE = "data/suggestions.json"
ADMINS = [5618445554, 879386491]

def register_suggestion(bot):
    @bot.message_handler(commands=['suggestion'])
    def handle_suggestion_command(message: Message):
        text = message.text.replace("/suggestion", "").strip()
        if text:
            save_suggestion(bot, message, text)
        else:
            msg = bot.send_message(
                message.chat.id,
                "💡 *Propose une suggestion !*\n\n👉 Réponds à ce message, ou utilise la commande comme ceci : `/suggestion Ta suggestion ici`",
                parse_mode="Markdown"
            )
            bot.register_next_step_handler(msg, ask_suggestion)

    def ask_suggestion(reply_msg: Message):
        @bot.message_handler(func=lambda m: m.reply_to_message and m.reply_to_message.message_id == reply_msg.message_id)
        def handle_reply(message: Message):
            save_suggestion(bot, message, message.text.strip())

def save_suggestion(bot, message, text):
    if not text:
        bot.send_message(message.chat.id, "❌ Suggestion vide. Réessaie.")
        return

    suggestion = {
        "user_id": message.from_user.id,
        "username": message.from_user.username or "",
        "first_name": message.from_user.first_name or "",
        "text": text,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    os.makedirs("data", exist_ok=True)
    try:
        with open(SUG_FILE, "r", encoding="utf-8") as f:
            all_sug = json.load(f)
    except FileNotFoundError:
        all_sug = []

    all_sug.append(suggestion)
    with open(SUG_FILE, "w", encoding="utf-8") as f:
        json.dump(all_sug, f, ensure_ascii=False, indent=2)

    bot.send_message(message.chat.id, "✅ Merci pour ta suggestion ! Elle a été enregistrée.")

    msg = (
        "💡 *Nouvelle suggestion reçue !*\n"
        f"👤 {suggestion['first_name']} (@{suggestion['username']})\n"
        f"📅 {suggestion['date']}\n"
        f"💬 Suggestion : {suggestion['text']}"
    )
    for admin_id in ADMINS:
        bot.send_message(admin_id, msg, parse_mode="Markdown")