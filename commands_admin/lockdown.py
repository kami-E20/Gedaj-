# commands_admin/lockdown.py

from telebot.types import Message
import json
import os

AUTHORIZED_ADMINS = [879386491, 5618445554]  # Kâmį & Anthony

LOCKDOWN_FILE = "data/lockdown_state.json"

def admin_only(handler):
    def wrapper(message: Message):
        if message.from_user.id not in AUTHORIZED_ADMINS:
            message.bot.send_message(
                message.chat.id,
                "🚫 Cette commande est réservée aux administrateurs du bot.\n\n"
                "📬 Si vous avez une suggestion ou un problème :\n"
                "• Utilisez /call pour contacter un admin\n"
                "• Partagez votre /avis\n"
                "• Ou proposez une /suggestion\n\n"
                "Merci pour votre compréhension 🙏"
            )
            return
        return handler(message)
    return wrapper

def set_lockdown_state(active: bool):
    os.makedirs("data", exist_ok=True)
    with open(LOCKDOWN_FILE, "w") as f:
        json.dump({"active": active}, f)

def get_lockdown_state() -> bool:
    if not os.path.exists(LOCKDOWN_FILE):
        return False
    with open(LOCKDOWN_FILE, "r") as f:
        data = json.load(f)
        return data.get("active", False)

def register_lockdown(bot):

    @bot.message_handler(commands=['lockdown'])
    @admin_only
    def handle_lockdown(message: Message):
        if 'off' in message.text.lower():
            set_lockdown_state(False)
            bot.send_message(message.chat.id, "🔓 Mode confinement *désactivé*. Le bot est à nouveau disponible.", parse_mode="Markdown")
        else:
            set_lockdown_state(True)
            bot.send_message(message.chat.id, "🔒 Mode confinement *activé*. Certaines commandes sont temporairement désactivées.", parse_mode="Markdown")