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
        jour = datetime.now().day
        with open(f"data/films/{jour}.json", "r", encoding="utf-8") as f:
            film = json.load(f)

        message = (
            f"🎬 *Film du jour* – {film.get('titre', 'Inconnu')}\n"
            f"📝 {film.get('description', 'Pas de description')}\n\n"
            "❤️ Réagissez si vous voulez le lien de téléchargement !"
        )

        sent = bot.send_message(
            os.getenv("CHANNEL_ID", "@GEEKMANIA"),
            message,
            parse_mode="Markdown"
        )

        # 🔒 Enregistrer le message pour le suivi des réactions
        film_msg_data = {
            "message_id": sent.message_id,
            "chat_id": sent.chat.id,
            "jour": jour
        }

        with open("data/film_message.json", "w", encoding="utf-8") as f:
            json.dump(film_msg_data, f, ensure_ascii=False, indent=2)

        print("🎬 Film du jour publié et message_id enregistré")

    except Exception as e:
        print("❌ Erreur publication film :", e)


def publier_quiz(bot: TeleBot):
    try:
        jour = datetime.now().day
        with open(f"data/quiz/quiz_{jour}.json", "r", encoding="utf-8") as f:
            quiz = json.load(f)

        bot.send_message(
            os.getenv("CHANNEL_ID", "@GEEKMANIA"),
            f"🧠 *Quiz du jour :* {quiz['question']}",
            parse_mode="Markdown"
        )
        print("❓ Quiz du jour publié")

    except Exception as e:
        print("❌ Erreur publication quiz :", e)


def publier_correction(bot: TeleBot):
    try:
        jour = datetime.now().day
        with open(f"data/quiz/quiz_{jour}.json", "r", encoding="utf-8") as f:
            quiz = json.load(f)

        bot.send_message(
            os.getenv("CHANNEL_ID", "@GEEKMANIA"),
            f"✅ Réponse correcte : {quiz['reponse']}"
        )
        print("✅ Correction du quiz envoyée")

    except Exception as e:
        print("❌ Erreur publication correction :", e)


def sauvegarder_donnees(bot: TeleBot):
    try:
        backup_donnees(bot)
        print("💾 Sauvegarde terminée")
    except Exception as e:
        print("❌ Erreur sauvegarde :", e)


def envoyer_statistiques(bot: TeleBot):
    try:
        bot.send_message(
            os.getenv("CHANNEL_ID", "@GEEKMANIA"),
            "📊 Résumé hebdomadaire disponible bientôt !"
        )
        print("📊 Statistiques hebdomadaires envoyées")
    except Exception as e:
        print("❌ Erreur statistiques :", e)


def publier_meilleurs_abonnes_fn(bot: TeleBot):
    try:
        publier_meilleurs_abonnes(bot)
        print("🏆 Meilleurs abonnés publiés")
    except Exception as e:
        print("❌ Erreur top abonnés :", e)


def publier_abonnes_du_mois_fn(bot: TeleBot):
    try:
        publier_abonnes_du_mois(bot)
        print("🎉 Abonnés du mois publiés")
    except Exception as e:
        print("❌ Erreur abonnés du mois :", e)