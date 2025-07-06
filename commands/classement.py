import json

def register_classement(bot):
    @bot.message_handler(commands=['classement'])
    def handle(message):
        try:
            with open("data/ranking.json", "r") as f:
                scores = json.load(f)
            top = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:5]
            if not top:
                bot.reply_to(message, "Aucun classement pour le moment.")
                return
            msg = "🏆 Classement des meilleurs abonnés :\n\n"
            for i, (user_id, pts) in enumerate(top, 1):
                msg += f"{i}. ID {user_id} — {pts} pts\n"
            bot.reply_to(message, msg)
        except Exception as e:
            bot.reply_to(message, "Erreur lors du chargement du classement.")