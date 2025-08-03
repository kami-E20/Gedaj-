import os
from loader import bot
from commands import register_user_commands
from commands_admin import register_admin_commands
from commands.listener import handle_reactions  # ✅ listener (gestion des réactions du canal)
from scripts import (  # ✅ grâce à __init__.py de scripts, import groupé
    backup_donnees,
    sauvegarder_donnees,
    sauvegarder_points_utilisateurs
)

def main():
    # ✅ Enregistrement des commandes utilisateur et admin
    register_user_commands(bot)
    register_admin_commands(bot)

    # ✅ Démarrage du listener pour les réactions dans le canal (déjà importé donc activé)
    print("🎧 Récepteur de réactions activé.")

    # ✅ Sauvegarde initiale de sécurité
    sauvegarder_points_utilisateurs()
    backup_donnees(bot)

    # ✅ Lancement du bot
    print("✅ GedajBot est maintenant en ligne.")
    bot.infinity_polling(skip_pending=True)

if __name__ == "__main__":
    main()