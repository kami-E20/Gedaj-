from scripts.points import ajouter_points

def register_listener(bot):
    @bot.message_handler(func=lambda m: m.chat.type != "private")
    def handle_comment(message):
        ajouter_points(message.from_user.id, "commentaire")

    @bot.message_handler(content_types=['text'])
    def detect_like_reaction(message):
        if message.text in ["❤️", "👍"]:
            ajouter_points(message.from_user.id, "reaction")