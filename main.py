import os
from telebot import TeleBot
from loader import bot
from commands import register_user_commands
from commands_admin import register_admin_commands
from commands.reaction import register_reaction_handlers
from scripts.points_logic import sauvegarder_points_utilisateurs
from scripts.backup import backup_donnees

def main():
    # 🔧 Enregistrement des commandes utilisateurs et admin
    register_user_commands(bot)
    register_admin_commands(bot)

    # 🎧 Listeners (réactions, messages texte)
    register_reaction_handlers(bot)

    # 📦 Sauvegarde automatique des données au démarrage
    sauvegarder_points_utilisateurs()
    backup_donnees(bot)

    # 🚀 Démarrage du bot en polling
    print("✅ GedajBot est maintenant en ligne.")
    bot.infinity_polling(skip_pending=True)


if __name__ == "__main__":
    main()