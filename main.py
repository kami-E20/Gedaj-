import os
import threading
from flask import Flask
from loader import bot
from commands import register_user_commands
from commands_admin import register_admin_commands
from commands.listener import handle_reactions  # 🔁 Détection des réactions du canal
from commands.textlistener import register_text_listener  # 🧠 Interaction avec messages texte

from scripts.points_logic import sauvegarder_points_utilisateurs
from scripts.backup import backup_donnees

app = Flask(__name__)

@app.route('/')
def home():
    return "GedajBot est actif sur Render (polling)."

def run_bot():
    # ✅ Enregistrement des commandes utilisateurs et admin
    register_user_commands(bot)
    register_admin_commands(bot)

    # 🔁 Enregistrement manuel des listeners si pas inclus automatiquement
    register_text_listener(bot)  # messages texte
    # 🚫 handle_reactions est un handler direct, donc pas besoin d’appel supplémentaire

    # 🧠 Sauvegarde de sécurité
    sauvegarder_points_utilisateurs()
    backup_donnees(bot)

    # 🚀 Démarrage du polling
    print("✅ GedajBot est maintenant en ligne.")
    bot.infinity_polling(skip_pending=True)

def main():
    threading.Thread(target=run_bot).start()

    # Lancement du faux serveur Flask pour "tromper" Render
    port = int(os.environ.get("PORT", 10000))  # Render définira automatiquement PORT
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    main()