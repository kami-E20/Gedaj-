from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from uuid import uuid4

# Dictionnaire temporaire pour stocker les spoilers
spoilers = {}

def register_spoiler(bot):
    @bot.message_handler(commands=['spoiler'])
    def handle_spoiler(message):
        parts = message.text.split(' ', 1)

        if len(parts) < 2:
            bot.send_message(
                message.chat.id,
                "❌ Utilisation incorrecte.\n\nExemple : `/spoiler Le héros meurt à la fin.`",
                parse_mode="Markdown"
            )
            return

        spoiler_text = parts[1].strip()
        spoiler_id = str(uuid4())  # ID unique pour chaque spoiler

        spoilers[spoiler_id] = spoiler_text

        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("⚠️ Afficher le spoiler", callback_data=f"show_spoiler:{spoiler_id}"))

        bot.send_message(
            message.chat.id,
            "😶 *Un spoiler est caché ici...*\n\nClique sur le bouton ci-dessous si tu veux le révéler.",
            parse_mode="Markdown",
            reply_markup=markup
        )

    @bot.callback_query_handler(func=lambda call: call.data.startswith("show_spoiler:"))
    def show_spoiler(call):
        spoiler_id = call.data.split(":")[1]
        spoiler_text = spoilers.get(spoiler_id, "⚠️ Spoiler introuvable ou expiré.")

        bot.edit_message_text(
            f"💥 *{spoiler_text}*",
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            parse_mode="Markdown"
        )

        # Optionnel : supprimer le spoiler de la mémoire après affichage
        spoilers.pop(spoiler_id, None)