import json
import os

LOCKDOWN_FILE = "data/lockdown.json"
AUTHORIZED_ADMINS = [5618445554, 879386491]

def register_lockdown(bot):
    @bot.message_handler(commands=['lockdown'])
    def handle_lockdown(message):
        if message.from_user.id not in AUTHORIZED_ADMINS:
            bot.reply_to(message, "⛔ Cette commande est réservée aux admins.")
            return

        # Lire l'état actuel
        if os.path.exists(LOCKDOWN_FILE):
            with open(LOCKDOWN_FILE, "r", encoding="utf-8") as f:
                state = json.load(f)
        else:
            state = {"active": False}

        # Basculer le mode
        state["active"] = not state["active"]
        new_status = "activé 🔒" if state["active"] else "désactivé 🔓"

        # Sauvegarde
        with open(LOCKDOWN_FILE, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=2)

        bot.send_message(message.chat.id, f"🔐 Mode confinement {new_status}.")