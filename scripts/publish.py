from datetime import datetime
from scripts.backup_handler import backup_donnees
from scripts.points import publier_meilleurs_abonnes, publier_abonnes_du_mois
from scripts.admin_notify import send_admin_news
from telebot import TeleBot
import json
import os

def publier_actu_privee(bot: TeleBot):
    try:
        with open("data/actu_du_jour.json", "r", encoding="utf-8") as f:
            actu = json.load(f)
        send_admin_news(bot, actu, categorie="Actu quotidienne")
        print("🔔 Actu privée envoyée aux admins")
    except Exception as e:
        print("❌ Erreur envoi actu :", e)

def publier_film(bot: TeleBot):
    try:
        with open("data/films/{}.json".format(datetime.now().day), "r", encoding="utf-8") as f:
            film = json.load(f)
        message = (
            f"🎬 *Film du jour* – {film.get('titre', 'Inconnu')}\n"
            f"📝 {film.get('description', 'Pas de description')}\n\n"
            "❤️ Réagissez si vous voulez le lien de téléchargement !"
        )
        bot.send_message(os.getenv("CHANNEL_ID", "@GEEKMANIA"), message, parse_mode="Markdown")
        print("🎬 Film du jour publié")
    except Exception as e:
        print("❌ Erreur publication film :", e)

def publier_quiz(bot: TeleBot):
    try:
        with open("data/quiz/quiz_{}.json".format(datetime.now().day), "r", encoding="utf-8") as f:
            quiz = json.load(f)
        bot.send_message(os.getenv("CHANNEL_ID", "@GEEKMANIA"), f"🧠 *Quiz du jour :* {quiz['question']}", parse_mode="Markdown")
        print("❓ Quiz du jour publié")
    except Exception as e:
        print("❌ Erreur publication quiz :", e)

def publier_correction(bot: TeleBot):
    try:
        with open("data/quiz/quiz_{}.json".format(datetime.now().day), "r", encoding="utf-8") as f:
            quiz = json.load(f)
        bot.send_message(os.getenv("CHANNEL_ID", "@GEEKMANIA"), f"✅ Réponse correcte : {quiz['reponse']}")
        print("✅ Correction du quiz envoyée")
    except Exception as e:
        print("❌ Erreur publication correction :", e)

def sauvegarder_donnees(bot: TeleBot):
    backup_donnees(bot)

def envoyer_statistiques(bot: TeleBot):
    # à intégrer plus tard depuis un module de stats
    bot.send_message(os.getenv("CHANNEL_ID", "@GEEKMANIA"), "📊 Résumé hebdomadaire disponible bientôt !")
    print("📊 Statistiques hebdomadaires envoyées")

def publier_meilleurs_abonnes(bot: TeleBot):
    publier_meilleurs_abonnes()

def publier_abonnes_du_mois(bot: TeleBot):
    publier_abonnes_du_mois()