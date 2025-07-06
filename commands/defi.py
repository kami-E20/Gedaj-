import random
from scripts.points import ajouter_points

DEFI_DU_JOUR = [
    "📣 Partage le canal @Geekmania à un ami aujourd’hui !",
    "💬 Commente une actu du jour dans le groupe !",
    "🎬 Propose un film ou un anime via /suggestion",
    "📍 Réagis avec ❤️ à une publication du jour",
]

def register_defi(bot):
    @bot.message_handler(commands=['defi'])
    def handle_defi(message):
        import datetime
        random.seed(datetime.datetime.now().day)
        defi = random.choice(DEFI_DU_JOUR)
        bot.reply_to(message, f"🎯 Défi du jour :\n{defi}\n\n✅ Tu gagnes 3 points en l’accomplissant !")
        ajouter_points(message.from_user.id, "quiz_participation")