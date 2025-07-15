import json
import os
from datetime import datetime

RANKING_FILE = "data/ranking.json"
REACTIONS_FILE = "data/reaction_logs.json"

def register_fanpass(bot):
    @bot.message_handler(commands=['fanpass'])
    def handle_fanpass(message):
        user = message.from_user
        user_id = str(user.id)
        username = user.username or "—"
        first_name = user.first_name or "Utilisateur"

        # 📊 Charger les données
        ranking = load_json(RANKING_FILE)
        reactions = load_json(REACTIONS_FILE)

        # 🎯 Trouver les stats utilisateur
        user_points = ranking.get(user_id, {}).get("points", 0)
        last_active = ranking.get(user_id, {}).get("last_active", "Inconnu")

        # 🔄 Formater la date
        try:
            last_date = datetime.strptime(last_active, "%Y-%m-%d")
            delta_days = (datetime.now() - last_date).days
            last_active_text = (
                "aujourd’hui" if delta_days == 0 else
                "hier" if delta_days == 1 else
                f"il y a {delta_days} jours"
            )
        except:
            last_active_text = "non enregistrée"

        # ⭐ Calculer niveau d’engagement
        if user_points >= 100:
            niveau = "⭐⭐⭐⭐⭐"
            statut = "Ultra-fan 🔥"
        elif user_points >= 70:
            niveau = "⭐⭐⭐⭐"
            statut = "Fan engagé"
        elif user_points >= 40:
            niveau = "⭐⭐⭐"
            statut = "Membre fidèle"
        elif user_points >= 20:
            niveau = "⭐⭐"
            statut = "Nouveau fan"
        else:
            niveau = "⭐"
            statut = "Débutant"

        # 🏆 Calcul du classement
        top = sorted(ranking.items(), key=lambda x: x[1].get("points", 0), reverse=True)
        position = next((i + 1 for i, (uid, _) in enumerate(top) if uid == user_id), None)

        classement_text = (
            f"📊 Tu es actuellement *#{position}* dans le classement Geekmania !"
            if position and position <= 10 else
            "📌 Continue comme ça pour intégrer le top 10 !"
        )

        # 🧾 Réponse complète
        texte = (
            "🎟️ *Ton Fan Pass Geekmania*\n\n"
            f"👤 *Utilisateur :* {first_name} (@{username})\n"
            f"🏅 *Statut :* {statut}\n"
            f"🔥 *Dernière activité :* {last_active_text}\n"
            f"✨ *Niveau d’engagement :* {niveau}\n"
            f"🪙 *Points cumulés :* {user_points}\n\n"
            f"{classement_text}"
        )

        bot.send_message(message.chat.id, texte, parse_mode="Markdown")


def load_json(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}