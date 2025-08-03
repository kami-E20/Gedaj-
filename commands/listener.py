from telebot.types import MessageReactionUpdated
from loader import bot
from commands.reaction import get_reaction_type, REACTION_POINTS
from scripts.points_logic import update_points

CANAL_USERNAME = "geekmaniaOfficiel"  # ❗ Ne pas inclure le @ ici pour la comparaison

@bot.message_reaction_handler()
def handle_reactions(reaction: MessageReactionUpdated):
    user = reaction.from_user
    message = reaction.message
    new_reaction = reaction.new_reaction

    if not user or not new_reaction or not message:
        return

    chat = message.chat

    # ✅ Ne traiter que les réactions dans le canal officiel
    if chat.type != "channel" or chat.username != CANAL_USERNAME:
        return

    emoji = new_reaction.emoji
    reaction_type = get_reaction_type(emoji)

    if not reaction_type:
        return

    points = REACTION_POINTS.get(reaction_type, 0)
    update_points(user.id, points)
    print(f"🎯 Réaction dans le canal : {emoji} ({reaction_type}) → +{points} points à {user.id}")