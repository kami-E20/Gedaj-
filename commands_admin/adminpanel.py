# adminpanel.py

from telebot import types
from loader import bot
from scripts.publish import (
    publier_film,
    publier_quiz,
    publier_correction,
    publier_actu_privee,
    envoyer_statistiques,
    publier_meilleurs_abonnes,
    publier_abonnes_du_mois,
    sauvegarder_donnees
)
from scripts.backup import backup_donnees
from admin import is_admin


# === Commande principale ===
@bot.message_handler(commands=['adminpanel'])
def ouvrir_adminpanel(message):
    if not is_admin(message.from_user.id):
        bot.reply_to(message, "⛔ Accès refusé, vous n’êtes pas administrateur.")
        return

    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("📢 Publications", callback_data="menu_publications"),
        types.InlineKeyboardButton("📊 Statistiques", callback_data="menu_stats"),
        types.InlineKeyboardButton("📂 Sauvegardes", callback_data="menu_sauvegardes"),
        types.InlineKeyboardButton("🚀 Run All", callback_data="runall"),
    )
    bot.send_message(
        message.chat.id,
        "🎛️ **Panneau de contrôle Admin**\nChoisissez une section :",
        reply_markup=markup,
        parse_mode="Markdown"
    )


# === Sous-menus ===
def menu_publications(chat_id):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("🎬 Film", callback_data="film"),
        types.InlineKeyboardButton("🎲 Quiz", callback_data="quiz"),
        types.InlineKeyboardButton("✅ Correction", callback_data="correction"),
        types.InlineKeyboardButton("📰 Actu privée", callback_data="actu"),
        types.InlineKeyboardButton("⬅️ Retour", callback_data="back_main"),
    )
    bot.send_message(chat_id, "📢 **Menu Publications**", reply_markup=markup, parse_mode="Markdown")


def menu_stats(chat_id):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("📊 Statistiques", callback_data="stats"),
        types.InlineKeyboardButton("🏆 Meilleurs abonnés", callback_data="meilleurs"),
        types.InlineKeyboardButton("👑 Abonnés du mois", callback_data="mois"),
        types.InlineKeyboardButton("⬅️ Retour", callback_data="back_main"),
    )
    bot.send_message(chat_id, "📊 **Menu Statistiques**", reply_markup=markup, parse_mode="Markdown")


def menu_sauvegardes(chat_id):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("💾 Sauvegarde", callback_data="save"),
        types.InlineKeyboardButton("📂 Backup", callback_data="backup"),
        types.InlineKeyboardButton("⬅️ Retour", callback_data="back_main"),
    )
    bot.send_message(chat_id, "📂 **Menu Sauvegardes**", reply_markup=markup, parse_mode="Markdown")


# === Gestion des callbacks ===
@bot.callback_query_handler(func=lambda call: True)
def callback_adminpanel(call):
    if not is_admin(call.from_user.id):
        bot.answer_callback_query(call.id, "⛔ Vous n’êtes pas admin.")
        return

    action = call.data

    try:
        # Navigation
        if action == "menu_publications":
            menu_publications(call.message.chat.id)
            bot.answer_callback_query(call.id)
        elif action == "menu_stats":
            menu_stats(call.message.chat.id)
            bot.answer_callback_query(call.id)
        elif action == "menu_sauvegardes":
            menu_sauvegardes(call.message.chat.id)
            bot.answer_callback_query(call.id)
        elif action == "back_main":
            ouvrir_adminpanel(call.message)
            bot.answer_callback_query(call.id)

        # Actions Publications
        elif action == "film":
            publier_film(bot)
            bot.answer_callback_query(call.id, "🎬 Film publié !")
        elif action == "quiz":
            publier_quiz(bot)
            bot.answer_callback_query(call.id, "🎲 Quiz publié !")
        elif action == "correction":
            publier_correction(bot)
            bot.answer_callback_query(call.id, "✅ Correction publiée !")
        elif action == "actu":
            publier_actu_privee(bot)
            bot.answer_callback_query(call.id, "📰 Actu envoyée en privé !")

        # Actions Statistiques
        elif action == "stats":
            envoyer_statistiques(bot)
            bot.answer_callback_query(call.id, "📊 Statistiques envoyées !")
        elif action == "meilleurs":
            publier_meilleurs_abonnes(bot)
            bot.answer_callback_query(call.id, "🏆 Meilleurs abonnés publiés !")
        elif action == "mois":
            publier_abonnes_du_mois(bot)
            bot.answer_callback_query(call.id, "👑 Abonnés du mois publiés !")

        # Actions Sauvegardes
        elif action == "save":
            sauvegarder_donnees(bot)
            bot.answer_callback_query(call.id, "💾 Sauvegarde effectuée !")
        elif action == "backup":
            backup_donnees(bot)
            bot.answer_callback_query(call.id, "📂 Backup effectué !")

        # Run All
        elif action == "runall":
            publier_actu_privee(bot)
            publier_film(bot)
            publier_quiz(bot)
            publier_correction(bot)
            publier_meilleurs_abonnes(bot)
            publier_abonnes_du_mois(bot)
            envoyer_statistiques(bot)
            sauvegarder_donnees(bot)
            backup_donnees(bot)
            bot.answer_callback_query(call.id, "🚀 Toutes les tâches exécutées !")

        else:
            bot.answer_callback_query(call.id, "⚠️ Action inconnue.")

    except Exception as e:
        bot.answer_callback_query(call.id, f"❌ Erreur : {str(e)}")